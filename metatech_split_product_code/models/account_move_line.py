from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    default_code = fields.Char("Default Code", related="product_id.default_code")
