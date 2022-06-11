# -*- coding: utf-8 -*-
from odoo import models,fields

class servicios(models.Model):
    _name = 'gym.servicios'
    name = fields.Char(string='Clave del servicio', size=10, required="True")
    nombre = fields.Char(string='Nombre del servicio', size=60, required="True")
    costo = fields.Integer(string = 'Costo de la membresia')

    _sql_constraints = [
        ('unique_servicio', 'unique (name)', 'El servicio ya existe!')
    ]