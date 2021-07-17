# -*- coding:utf-8 -*-

from odoo import models,fields,api
from datetime import datetime

class Books(models.Model):
    _name = 'books'
    _rec_name = 'name_book'

    name_book = fields.Char('Tên Sách')
    author = fields.Char('Tác Giả')
    number_page = fields.Integer('Số Trang')
    category = fields.Many2one('book.category','Thể loại')
    num_in = fields.Integer('Số lượng nhập')
    num_remain = fields.Integer('Số lượng còn lại')
    # emp_borrow = fields.Many2one('tickets','Nhân viên mượn')
    emp_borrow = fields.One2many(comodel_name="tickets", inverse_name="name_emp", string="Nhân viên mượn")

    # emp_borrow = fields.One2many("book.line", "name_book", "Người mượn")

    @api.multi
    @api.depends("num_in")
    def _processing(self):
        for row in self:
            borrowedTrue = [lst.line for lst in row.emp_borrow]
            borrowed = len([record.name for record in borrowedTrue if record.status == False])
            row.num_remain = row.num_in - borrowed

    @api.constrains("num_page", "num_in")
    def _recvdate(self):
        # for row in self:
            if self.num_in <= 0:
                raise ValidationError("Số lượng sách nhập phải lớn hơn 0")

            if self.num_page < 5:
                raise ValidationError("Số trang phải lớn hơn 5")


