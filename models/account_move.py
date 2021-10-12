# -*- coding: utf-8 -*-


from odoo import fields, models, api, _
from odoo.exceptions import UserError


class AccountInvoiceRefund(models.TransientModel):

    _inherit = "account.invoice.refund"

    def invoice_refund(self):
        result = super(AccountInvoiceRefund, self).invoice_refund()
        id_nuevo = 0
        for tupla in result.get('domain'):
            if tupla[0] == 'id':
                id_nuevo = tupla[2][0]
        nota_rec = self.env['account.invoice'].browse(id_nuevo)
        nota_rec.account_id = nota_rec.company_id.account_credit_note_id
        for linea in nota_rec.invoice_line_ids:
            linea.account_id = nota_rec.company_id.account_credit_note_id
        return result
