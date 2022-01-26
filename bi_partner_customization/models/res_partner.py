from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    cin = fields.Many2many("ir.attachment", "partner_cin_ir_attachments_rel", string="CIN")
    banking_receipt = fields.Many2many("ir.attachment", "partner_br_ir_attachments_rel", string="Banking Receipt")
    payslip = fields.Many2many("ir.attachment", "partner_payslip_ir_attachments_rel", string="Payslip")

    def confirm_membership(self):
        pass