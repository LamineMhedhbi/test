from odoo import models, fields


class Region(models.Model):
    _name = "region"

    _sql_constraints = [("internal_division", "UNIQUE (name)", "Region Name should be unique!")]

    name = fields.Char(string="Region")
