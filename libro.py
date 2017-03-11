# -*- coding: utf-8 -*-

from openerp import models, fields, api

class libro(models.Model):
	_name = 'libro.jacob'
	_rec_name = "nombre_libro"
	nombre_libro = fields.Char('nombre del libro')
	fecha = fields.Date('fecha de publicacion')
	nombre_editorial = fields.Char('nombre editorial')
	nombre_autor = fields.Char('nombre del autor')
