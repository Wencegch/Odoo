from odoo import models, fields, api

class persona(models.Model):
	_name = 'ejemplo.persona'
	_description = 'model persona'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	fecha = fields.Char(string='Fecha',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
