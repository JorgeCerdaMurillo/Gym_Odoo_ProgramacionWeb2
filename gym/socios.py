# -*- coding: utf-8 -*-
from odoo import models,fields, api

class socios(models.Model):
    _name = 'gym.socios'
    _rec_name='nombre'
    name = fields.Char(string='NumSocio')
    nombre = fields.Char(string='Nombre y Apellidos')
    telefono = fields.Char(string='Teléfono')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    tiposocio = fields.Boolean(string='Estudiante?')
    servicio_id = fields.Many2one('gym.servicios',string="Servicio")
    fecha_i = fields.Char(string='Fecha de Inicio')
    fecha_f = fields.Char(string='Fecha de Finalizacion')
    _sql_constraints = [
        ('unique_socio', 'unique (name)', 'El socio ya existe!')
    ]