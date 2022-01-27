from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    name_prop = fields.Char("Name of the property")
    nbr_block = fields.Integer("Nbr of blocks")
    nbr_floor_block = fields.Integer("Nbr of floors by block")

    def confirm_membership(self):
        pass