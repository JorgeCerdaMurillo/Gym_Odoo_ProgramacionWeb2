from odoo import models,fields, api

class ventas(models.Model):
    _name = 'gym.ventas'
    name = fields.Char(string='NumVenta')
    nombre = fields.Many2one('gym.productos',string='Nombre del producto')
    socios = fields.Many2one('gym.socios',string='Socios')
    fecha = fields.Char(string='Fecha')
    costo = fields.Integer(string='Costo')
    cantidad = fields.Integer(string='Cantidad')
    
    _sql_constraints = [
        ('unique_ventas', 'unique (name)', 'El numero de la venta ya fue registrado!')
    ]