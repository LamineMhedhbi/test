from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    region_id = fields.Many2one("geographical.region", string="Region")

   