# -*- coding: utf-8 -*-
from odoo import models,fields, api

class productos(models.Model):
    _name = 'gym.productos'
    _rec_name='nombre'
    name = fields.Char(string='ID_Producto')
    nombre = fields.Char(string='Nombre Producto')
    precio = fields.Char(string='Precio')
    


    _sql_constraints = [
        ('unique_producto', 'unique (name)', 'El Producto ya existe!')
    ]
    