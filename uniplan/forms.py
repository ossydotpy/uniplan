from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Optional


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
    is_compulsory = IntegerField('Is Compulsory', validators=[Optional()])
    is_elective = IntegerField('Is Elective', validators=[Optional()])


class ProgramScholarshipForm(FlaskForm):
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    scholarship_id = IntegerField('Scholarship ID', validators=[DataRequired()])


class ProgramCareerForm(FlaskForm):
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    career = StringField('Career', validators=[DataRequired()])
