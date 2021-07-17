# -*- coding:utf-8 -*-

from odoo import models,fields

class BookCategory(models.Model):
    _name = 'book.category'
    _rec_name = 'name_category'


    name_category = fields.Char('Loại Sách')
    desc = fields.Text('Mô tả thể loại sách')