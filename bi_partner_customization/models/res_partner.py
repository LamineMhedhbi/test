from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    photo1 = fields.Many2many("ir.attachment", "partner_cin_ir_attachments_rel", string="Photo 1")
    photo2 = fields.Many2many("ir.attachment", "partner_br_ir_attachments_rel", string="Photo 2")
    photo3 = fields.Many2many("ir.attachment", "partner_payslip_ir_attachments_rel", string="Photo 3")

    def confirm_membership(self):
        pass