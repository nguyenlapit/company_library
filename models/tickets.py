# -*- coding:utf-8 -*-

from odoo import models,fields,api
from datetime import datetime

class Ticket(models.Model):
    _name = 'tickets'
    _rec_name = 'name_emp'

    code_emp = fields.Char('Mã Nhân Viên')
    name_emp = fields.Char('Tên Nhân Viên')
    sdt = fields.Char('Số Điện Thoại')
    date_borrow = fields.Date('Thời gian mượn sách')
    date_pay = fields.Date('Thời gian trả sách')
    line_ids = fields.One2many('book.line','line','Sách Mượn')

class BookLine(models.Model):
    _name = 'book.line'
    _rec_name = 'line'

    line = fields.Many2one('tickets')
    name_book = fields.Many2one('books','Tên Sách')
    author1 = fields.Char('Tên Tác Giả')

    @api.onchange('name_book')
    def onchange_book(self):
        if self.name_book is not None:
            self.author1 = self.name_book.author