# -*- coding: utf-8 -*-
from odoo import models,fields, api

class instructores(models.Model):
    _name = 'gym.instructores'

    name = fields.Char(string='ID_Instructor')
    nombre_inst = fields.Char(string='Nombre y Apellidos')
    telefono = fields.Char(string='Teléfono')
    horario = fields.Char(string='Horario')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    especialidad = fields.Integer(string='Especialidad')

    _sql_constraints = [
        ('unique_instructor', 'unique (name)', 'El Instructor ya existe!')
    ]

