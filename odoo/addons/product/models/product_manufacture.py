# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductManufacture(models.Model):
    _name = 'product.manufacture'
    _description = 'Product Manufacture'

    name = fields.Char(string='Manufacture name', required = True)
    models_id = fields.One2many('product.model', 'product_manufacture_id', 'Models', help="One manufacture for many models")

