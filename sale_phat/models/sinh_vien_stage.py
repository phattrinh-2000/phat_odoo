from odoo import models, fields

class SinhVienStage(models.Model):
    _name = 'sinh.vien.stage'
    _description = 'Sinh Vien Stage'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    fold = fields.Boolean(string='Folded in Kanban', default=False)
