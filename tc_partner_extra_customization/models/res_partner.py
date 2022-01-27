from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    region = fields.Many2one("region", string="Region")

   