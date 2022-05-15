from odoo import models,fields, api

class compras(models.Model):
    _name = 'gym.compras'
    name = fields.Char(string='NumCompra')
    nombre = fields.Char(string='Nombre del producto')
    provedor = fields.Char(string='Provedor')
    fecha = fields.Char(string='Fecha')
    costo = fields.Integer(string='Costo')
    cantidad = fields.Integer(string='Cantidad')
    
    _sql_constraints = [
        ('unique_compras', 'unique (name)', 'El numero de compra ya fue registrado!')
    ]