# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class Name(models.AbstractModel):
    report_name = 'module.name_report'
    _name = 'report.%s' % report_name

    @api.multi
    def render_html(self, docids, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name(self.report_name)
        docs = self.env[report.model].browse(docids)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
        }
        return report_obj.render(self.report_name, docargs)
