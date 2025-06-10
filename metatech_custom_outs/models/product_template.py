from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends('name')
    def _compute_display_name(self):
        for template in self:
            template.display_name = False if not template.name else template.name
