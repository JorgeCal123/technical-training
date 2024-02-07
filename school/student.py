from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age')
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        today = fields.Date.today()
        for student in self:
            if student.birth_date:
                delta = today - student.birth_date
                student.age = delta.days // 365
