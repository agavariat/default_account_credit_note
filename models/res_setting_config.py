# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    account_credit_note_id = fields.Many2one(related='company_id.account_credit_note_id', comodel_name='account.account',
                                             string="Default account for credit notes", store=True, readonly=False)