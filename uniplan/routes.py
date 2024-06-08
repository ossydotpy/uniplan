from flask import render_template, redirect, url_for
from uniplan import app, db
from uniplan.models import Program, Subject, ProgramSubject
from uniplan.forms import ProgramForm, SubjectForm, ProgramSubjectForm


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

# @app.route('/delete_prog/<int:program_id>', methods=['POST'])
# def delete_program(program_id):
#     program = ProgramSubject.query.get_or_404(program_id)
#     db.session.delete(program)
#     db.session.commit()
#     return redirect(url_for('manage_programs'))
