# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductModel(models.Model):
    _name = 'product.model'
    _description = 'Product Model'

    name = fields.Char(string='Model name', required = True)
    product_manufacture_id = fields.Many2one('product.manufacture', 'Product Manufacture', index=True, ondelete='Set Null')