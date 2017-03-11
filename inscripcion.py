# -*- coding: utf-8 -*-

from openerp import models, fields, api

class inscripcion(models.Model):
	_name = 'inscripcion.jacob'

	nombre_usuario = fields.Char('nombre de usuario')
	libro = fields.Many2one('libro.jacob','Nombre del Libro')
	cedula = fields.Integer('cedula de usuario')
	telefono = fields.Integer('numero de telefono')
	direccion = fields.Char('direccion de usuario')
