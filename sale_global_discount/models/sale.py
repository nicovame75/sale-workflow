# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount = fields.Float(
        digits=dp.get_precision('Discount'),
        default=0.0,
        string='Discount (%)',
    )
    amount_discount = fields.Float(
        string='Amount Discount',
        store=True,
        compute='_amount_all',
    )

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            super(SaleOrder, self)._amount_all()
            if not order.amount_discount:
                continue
            order.amount_discount = order.pricelist_id.currency_id.round(sum([
                        x.amount_order_discount for x in order.order_line]))


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    amount_order_discount = fields.Monetary(
        compute='_compute_amount',
        string='Discount',
        readonly=True,
        store=True,
    )

    @api.depends('order_id.discount')
    def _compute_amount(self):
        for line in self:
            line_discount = line.discount
            line_price_unit = line.price_unit
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            amount_discount = price * line.order_id.discount / 100
            price_wo_discount = price - amount_discount
            line.update({
                'price_unit': price_wo_discount,
                'amount_order_discount': amount_discount,
                'discount': 0.0,
            })
            super(SaleOrderLine, self)._compute_amount()
            line.update({
                'price_unit': line_price_unit,
                'discount': line_discount,
            })

    @api.depends('order_id.discount')
    def _get_price_reduce(self):
        for line in self:
            super(SaleOrderLine, self)._get_price_reduce()
            if line.order_id.discount:
                line.price_reduce *= (1 - line.order_id.discount / 100)
