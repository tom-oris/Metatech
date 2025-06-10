from odoo import fields, models


class ApprovalProductLine(models.Model):
    _inherit = "approval.product.line"

    default_code = fields.Char("Default Code", related="product_id.default_code")
