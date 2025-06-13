from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    image_product = fields.Image(string="Image Product")
    note_product = fields.Char(string="Note Product")
    note_tech = fields.Char(string="Note Tech")
    amount_content = fields.Float(string="Amount Content")
    vendor_id = fields.Many2one("res.vendor", string="Vendor")
