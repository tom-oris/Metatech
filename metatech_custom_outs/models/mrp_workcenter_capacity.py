from odoo import fields, models


class MRPWorkCenterCapacity(models.Model):
    _inherit = "mrp.workcenter.capacity"

    default_code = fields.Char("Default Code", related="product_id.default_code")
