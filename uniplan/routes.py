import csv
from functools import wraps

from flask import render_template, redirect, url_for, request, flash
from uniplan import app, db
from uniplan.models import Program, Subject, ProgramSubject, Scholarship, ProgramScholarship
from uniplan.forms import ProgramForm, SubjectForm, ProgramSubjectForm, ScholarshipForm, ProgramScholarshipForm


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/program_management', methods=['GET'])
def manage_programs():
    programs = Program.query.all()
    return render_template('manage_prog.html', programs=programs)


@app.route('/add_program', methods=['GET', 'POST'])
def add_program():
    form = ProgramForm()
    if form.validate_on_submit():
        program_name = form.program_name.data
        field = form.field.data
        department = form.department.data
        university = form.university.data
        description = form.description.data
        tuition_fees = form.tuition_fees.data

        new_program = Program(program_name=program_name, field=field, department=department,
                              university=university, description=description, tuition_fees=tuition_fees)
        db.session.add(new_program)
        db.session.commit()
        return redirect(url_for('manage_programs'))
    return render_template('add_program.html', form=form)


@app.route('/manage_sub', methods=['GET', 'POST'])
def manage_sub():
    subjects = Subject.query.all()
    form = SubjectForm()
    if form.validate_on_submit():
        subject_name = form.subject_name.data
        new_subject = Subject(subject_name=subject_name)
        db.session.add(new_subject)
        db.session.commit()
        return redirect(url_for('manage_sub'))
    return render_template('manage_sub.html', form=form, subjects=subjects)


@app.route('/scholarships', methods=['GET', 'POST'])
def scholarships():
    scholarship_list = Scholarship.query.all()
    form = ScholarshipForm()
    if form.validate_on_submit():
        scholarship_name = form.scholarship_name.data
        description = form.description.data
        amount = form.amount.data
        eligibility = form.eligibility.data
        website = form.website.data
        new_scholarship = Scholarship(scholarship_name=scholarship_name, description=description,
                                      amount=amount, eligibility=eligibility, website=website)
        db.session.add(new_scholarship)
        db.session.commit()
        return redirect(url_for('scholarships'))
    return render_template('scholarships.html', form=form, scholarships=scholarship_list)


@app.route('/prog_scholar', methods=['GET', 'POST'])
def prog_scholar():
    programs = Program.query.all()
    prog_scho = ProgramScholarship.query.all()
    form = ProgramScholarshipForm()
    if form.validate_on_submit():
        program_id = form.program_id.data
        scholarship_id = form.scholarship_id.data

        new_prog_scho = ProgramScholarship(program_id=program_id, scholarship_id=scholarship_id)
        db.session.add(new_prog_scho)
        db.session.commit()
        return redirect(url_for('prog_scholar'))

    return render_template('prog_scho.html', form=form, prog_scho=prog_scho, programs=programs)


@app.route('/prog_sub', methods=['GET', 'POST'])
def manage_prog_sub():
    programs = Program.query.all()
    prog_subs = ProgramSubject.query.all()
    form = ProgramSubjectForm()
    if form.validate_on_submit():
        program_id = form.program_id.data
        subject_id = form.subject_id.data
        cutoff = form.cutoff.data
        is_compulsory = form.is_compulsory.data
        is_elective = form.is_elective.data

        new_prog_sub = ProgramSubject(program_id=program_id, subject_id=subject_id, cutoff=cutoff,
                                      is_compulsory=is_compulsory, is_elective=is_elective)
        db.session.add(new_prog_sub)
        db.session.commit()
        return redirect(url_for('manage_prog_sub'))

    return render_template('prog_sub.html', form=form, prog_subs=prog_subs, programs=programs)


@app.route('/delete_sub/<int:subject_id>', methods=['POST'])
def delete_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for('manage_sub'))


@app.route('/delete_prog/<int:program_id>', methods=['POST'])
def delete_program(program_id):
    program = Program.query.get_or_404(program_id)
    db.session.delete(program)
    db.session.commit()
    return redirect(url_for('manage_programs'))


@app.route('/bulk_add', methods=['POST', 'GET'])
def bulk_add():
    return render_template('bulk_add.html')


def extract_csv_content(file):
    csv_content = []
    file.seek(0)
    csv_reader = csv.reader((line.decode('utf-8') for line in file))
    header = next(csv_reader)
    for row in csv_reader:
        csv_content.append(row)
    return header, csv_content


def handle_csv_upload():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            file = request.files['file']
            print('recieved file')

            if not file:
                flash('No selected file/invalid file type')
                return redirect(request.url)

            csv_content = extract_csv_content(file)
            return f(csv_content, *args, **kwargs)
        return decorated_function
    return decorator


@app.route('/add_prog_excel', methods=['GET', 'POST'])
@handle_csv_upload()
def add_prog_excel(csv_content):
    expected_columns = ['program_id', 'program_name', 'field', 'department', 'university', 'description', 'tuition_fees']
    header, rows = csv_content

    if header == expected_columns:
        for program in rows:
            new_program = Program(program_name=program[1],
                                  field=program[2],
                                  department=program[3],
                                  university=program[4],
                                  description=program[5],
                                  tuition_fees=program[6])
            db.session.add(new_program)
        db.session.commit()
    else:
        flash('column mismatch')
    return redirect(url_for('manage_programs'))