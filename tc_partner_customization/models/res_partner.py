from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    field1 = fields.Char("Field 1")
    field2 = fields.Char("Field 2")
    field3 = fields.Char("Field 3")

    def confirm_membership(self):
        pass