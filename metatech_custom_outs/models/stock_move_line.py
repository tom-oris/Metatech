from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    default_code = fields.Char("Default Code", related="product_id.default_code")
