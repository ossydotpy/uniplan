from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Optional, ValidationError

from uniplan.models import Program, Subject


class ProgramForm(FlaskForm):
    program_name = StringField('Program Name', validators=[DataRequired()])
    field = StringField('Field', validators=[Optional()])
    department = StringField('Department', validators=[Optional()])
    university = StringField('University', validators=[Optional()])
    description = TextAreaField('Description', validators=[Optional()])
    tuition_fees = IntegerField('Tuition Fees', validators=[Optional()])


class SubjectForm(FlaskForm):
    subject_name = StringField('Subject Name', validators=[DataRequired()])


class ScholarshipForm(FlaskForm):
    scholarship_name = StringField('Scholarship Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    amount = IntegerField('Amount', validators=[Optional()])
    eligibility = TextAreaField('Eligibility', validators=[Optional()])
    website = StringField('Website', validators=[Optional()])


class ProgramSubjectForm(FlaskForm):
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    subject_id = IntegerField('Subject ID', validators=[DataRequired()])
    cutoff = IntegerField('Cutoff', validators=[Optional()])
    is_compulsory = BooleanField('Is Compulsory')
    is_elective = BooleanField('Is Elective')

    def validate_program_id(self, field):
        program = Program.query.get(field.data)
        if program is None:
            raise ValidationError('Invalid Program ID')

    def validate_subject_id(self, field):
        subject = Subject.query.get(field.data)
        if subject is None:
            raise ValidationError('Invalid Subject ID')


class ProgramScholarshipForm(FlaskForm):
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    scholarship_id = IntegerField('Scholarship ID', validators=[DataRequired()])

    def validate_program_id(self, field):
        program = Program.query.get(field.data)
        if program is None:
            raise ValidationError('Invalid Program ID')


class ProgramCareerForm(FlaskForm):
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    career = StringField('Career', validators=[DataRequired()])

    def validate_program_id(self, field):
        program = Program.query.get(field.data)
        if program is None:
            raise ValidationError('Invalid Program ID')
