# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Global Discount',
    'summary': 'Discount per sale order',
    'version': '11.0.1.0.0',
    'development_status': 'Alpha',
    'category': 'Sales',
    'website': 'https://github.com/OCA/sale-workflow',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale',
    ],
    'data': [
        # 'security/some_model_security.xml',
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        # 'views/res_partner_view.xml',
    ],
}
