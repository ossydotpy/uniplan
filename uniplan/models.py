from flask_sqlalchemy import SQLAlchemy
from uniplan import db


class Program(db.Model):
    __tablename__ = 'program'

    program_id = db.Column(db.Integer, primary_key=True, unique=True)
    program_name = db.Column(db.Text, nullable=False)
    field = db.Column(db.Integer)
    department = db.Column(db.Text)
    university = db.Column(db.Text)
    description = db.Column(db.Text)
    tuition_fees = db.Column(db.Integer)


class Subject(db.Model):
    __tablename__ = 'subject'

    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    subject_name = db.Column(db.Text)


class Scholarship(db.Model):
    __tablename__ = 'scholarship'

    scholarship_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    scholarship_name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    amount = db.Column(db.Integer)
    eligibility = db.Column(db.Text)
    website = db.Column(db.Text)


class ProgramSubject(db.Model):
    __tablename__ = 'program_subject'

    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.subject_id'), primary_key=True)
    cutoff = db.Column(db.Integer)
    is_compulsory = db.Column(db.Integer, default=0)
    is_elective = db.Column(db.Integer, default=1)

    program = db.relationship('Program', backref=db.backref('program_subjects', cascade='all, delete-orphan'))
    subject = db.relationship('Subject', backref=db.backref('program_subjects', cascade='all, delete-orphan'))


class ProgramScholarship(db.Model):
    __tablename__ = 'program_scholarship'

    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), primary_key=True)
    scholarship_id = db.Column(db.Integer, db.ForeignKey('scholarship.scholarship_id'), primary_key=True)

    program = db.relationship('Program', backref=db.backref('program_scholarships', cascade='all, delete-orphan'))
    scholarship = db.relationship('Scholarship', backref=db.backref('program_scholarships', cascade='all, delete-orphan'))


class ProgramCareer(db.Model):
    __tablename__ = 'program_career'

    program_id = db.Column(db.Integer, primary_key=True)
    career = db.Column(db.Text)

    program = db.relationship('Program', backref=db.backref('program_careers', cascade='all, delete-orphan'))

    __table_args__ = (
        db.ForeignKeyConstraint(['program_id'], ['program.program_id']),
    )
