from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    default_code = fields.Char("Default Code", related="product_id.default_code")
