from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    default_code = fields.Char("Default Code", related="product_id.default_code")
