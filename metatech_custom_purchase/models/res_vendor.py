from odoo import fields, models


class ResVendor(models.Model):
    _name = "res.vendor"
    _description = "Res Vendor"

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'The name must be unique'),
    ]
