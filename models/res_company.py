# -*- coding: utf-8 -*-
from odoo import fields, models, api,_

class ResCompany(models.Model):
    _inherit = 'res.company'

    account_credit_note_id = fields.Many2one(comodel_name='account.account', string='Default account for credit notes')