# -*- coding: utf-8 -*-
import requests

from odoo import models, fields
from odoo.tools.translate import _


class intranet_partner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'

    intranet_register_link = fields.Char(string=_("Register intranet link"))
    firebase_uid = fields.Char(string=_("Firebase uid"))
