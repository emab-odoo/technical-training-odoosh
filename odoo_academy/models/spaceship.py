
# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Spaceship(models.Model):
    _name = "academy.spaceship"
    _description = "Wuuu spaceships"
    
    name = fields.Char(string="Title", required=True)
    description=fields.Text(string="Description")
    type=fields.Selection(string="Type", selection=[('small', 'Small'), ('large', 'Large')], copy=False)
    numberOfPassengers=fields.Integer(string="Number of passengers", default=1)
    
    