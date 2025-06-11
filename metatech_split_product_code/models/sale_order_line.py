from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    default_code = fields.Char("Default Code", related="product_id.default_code")
