from odoo import fields, models


class MRPBomLine(models.Model):
    _inherit = "mrp.bom.line"

    default_code = fields.Char("Default Code", related="product_id.default_code")
