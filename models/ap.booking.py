from odoo import models, fields


class SaleOrderInherit(models.Model):
    _inherit = 'hr.applicant'
