# -*- coding: utf-8 -*-
from odoo import models, fields


class SinhVien(models.Model):
    _name = 'sinh.vien'
    _description = 'Sinh Vien'

    name = fields.Char(string='Sinh Vien', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    image = fields.Binary(string='Image')
    lop = fields.Char(string='Lop')
    day_of_birth = fields.Date(string='Day of Birth')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True)
    stage_id = fields.Many2one('sinh.vien.stage', string='Stage')
    subjects = fields.One2many('bang.diem', 'student_id', string='Subjects and Grades')


class BangDiem(models.Model):
    _name = 'bang.diem'
    _description = 'Bang Diem'

    name = fields.Char(string='Subject Name', required=True)
    grade = fields.Char(string='Grade')
    student_id = fields.Many2one('sinh.vien', string='Student')
