<<<<<<< HEAD
from datetime import datetime

from flask import jsonify, render_template, request, flash, redirect, url_for
from flask_login import (
  login_required, current_user
)

from app import db
from app.base.models import Batch, Semester
from app.student import blueprint
from app.student.forms import CreateStudentForm, CreateRankForm, CreateChargeTableForm
from app.student.models import Student, Rank, ChargeTable, StudentSummary
=======
from flask import jsonify, render_template, request, flash, redirect, url_for
from flask_login import (
  login_required,
  current_user
)

from app import db
from app.student import blueprint
from app.student.models import Student, Rank, ChargeTable
from app.student.forms import CreateStudentForm, CreateRankForm, CreateChargeTableForm
from app.base.models import Batch, Semester
from datetime import datetime


# @blueprint.route('/<template>')
# @login_required
# def route_template(template):
#     return render_template(template + '.html')
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484


@blueprint.route('/fixed_<template>')
@login_required
def route_fixed_template(template):
    return render_template('fixed/fixed_{}.html'.format(template))


@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))


@blueprint.route('/charge_tables')
@login_required
def get_all_charge_tables():
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    charge_tables = db.session.query(ChargeTable).all()
    return render_template('charge_table.html', charge_tables=charge_tables)


@blueprint.route('charge_table/<charge_id>', methods=['GET', 'POST'])
@login_required
def update_charge_table(charge_id):
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    form = CreateChargeTableForm(request.form)
    charge_table = ChargeTable.query.filter_by(id=charge_id).first()
    if request.method == 'GET':
        return render_template('/update_charge_table.html', form=form, charge_table=charge_table)
    else:
        price = request.form['price']
        charge_table.price = price
        charge_table.updated_at = datetime.now()
        db.session.merge(charge_table)
    db.session.commit()
    flash('Charge table updated')
    return redirect('/student/charge_tables')


<<<<<<< HEAD
@blueprint.route('charge_table/create', methods=['GET', 'POST'])
@login_required
def create_charge_table():
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
@blueprint.route('/charge_table/create', methods=['GET', 'POST'])
@login_required
def create_charge_table():
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    if request.method == 'GET':
        form = CreateChargeTableForm(request.form)
        return render_template('create_charge_table.html', form=form)
    price = request.form['price']
    department = request.form['department']
    batch = request.form['batch']
    semester = request.form['semester']
    rank = request.form['rank']
    is_duplicate = ChargeTable.query.filter_by(department_id=department,
                                               batch_id=batch,
<<<<<<< HEAD
                                               semester_id=semester,
                                               rank_id=rank).first()
=======
                                               semester_id=semester).first()
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    if is_duplicate is None:
        charge_table = ChargeTable(price, department, batch, semester, rank)
        charge_table.created_at = datetime.now()
        db.session.add(charge_table)
        db.session.commit()
        flash('Charge table created')
        return redirect('/student/charge_tables')
    else:
        form = CreateChargeTableForm(request.form)
        error = 'Duplicate entry'
        return render_template('create_charge_table.html', error=error, form=form)


@blueprint.route('/ranks')
@login_required
def get_all_ranks():
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    ranks = db.session.query(Rank).all()
    return render_template('rank.html', ranks=ranks)


@blueprint.route('/rank/delete<rank_id>')
@login_required
def delete_rank(rank_id):
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    try:
        Rank.query.filter_by(id=rank_id).delete()
        db.session.commit()
        flash('Rank deleted!')
        return redirect('/student/ranks')
    except Exception as e:
        print(e)
        error = 'Delete error! some entities are referring to it.'
        flash(error, 'error')
        return redirect('/student/ranks')


@blueprint.route('rank/<rank_id>', methods=['GET', 'POST'])
@login_required
def update_rank(rank_id):
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    form = CreateRankForm(request.form)
    rank = Rank.query.filter_by(id=rank_id).first()
    if request.method == 'GET':
        return render_template('/update_rank.html', form=form, rank=rank)
    else:
        name = request.form['name']
        code = request.form['code']
        description = request.form['description']
        rank.name = name
        rank.code = code
        rank.description = description
        rank.updated_at = datetime.now()
        db.session.merge(rank)
    db.session.commit()
    flash('Rank updated')
    return redirect('/student/ranks')


@blueprint.route('/rank/create', methods=['GET', 'POST'])
@login_required
def create_rank():
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    if request.method == 'GET':
        rank_form = CreateRankForm(request.form)
        return render_template('create_rank.html', rank_form=rank_form)
    name = request.form['name']
    code = request.form['code']
    description = request.form['description']
    check_name = Rank.query.filter_by(name=name).first()
    check_code = Rank.query.filter_by(code=code).first()
    if check_name is None and check_code is None:
        rank = Rank(name, code, description)
        rank.created_at = datetime.now()
        db.session.add(rank)
        db.session.commit()
        flash('Rank created')
        return redirect('/student/ranks')
    else:
        rank_form = CreateRankForm(request.form)
        error = 'Duplicate entry'
        return render_template('create_rank.html', error=error, rank_form=rank_form)


@blueprint.route('/students')
@login_required
def get_all_students():
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        students = Student.query.filter_by(id=current_user.student.id).all()
        return render_template('student.html', students=students)
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    students = db.session.query(Student).all()
    return render_template('student.html', students=students)


@blueprint.route('/delete<student_id>')
@login_required
def delete_student(student_id):
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    try:
        Student.query.filter_by(id=student_id).delete()
        db.session.commit()
        flash('Student deleted!')
        return redirect('students')
    except Exception as e:
        print(e)
        flash('Delete error!')
        return redirect('students')


@blueprint.route('/get_batch/<department_id>')
@login_required
def get_batch(department_id):
    try:
        batches = Batch.query.filter_by(department_id=department_id).all()
    except Exception as e:
        print(e)
        return {'code': 400}
    dic = {}
    for i in batches:
        print(i)
        dic[str(i.id)] = {
          'name': i.name
        }
    dic['code'] = 200
    a = jsonify(dic)
    print(a)
    return a


@blueprint.route('/get_semester/<batch_id>')
@login_required
def get_semester(batch_id):
    try:
        semesters = Semester.query.filter_by(batch_id=batch_id).all()
    except Exception as e:
        print(e)
        return {'code': 400}
    dic = {}
    for i in semesters:
        print(i)
        dic[str(i.id)] = {
          'name': i.name
        }
    dic['code'] = 200
    res = jsonify(dic)
    print(res)
    return res


@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create_student():
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    student_form = CreateStudentForm(request.form)
    if request.method == 'GET':
        return render_template('/create_student.html', student_form=student_form)
    name = request.form['name']
    gender = request.form['gender']
    roll = request.form['roll_number']
    user = request.form['user']
    batch = request.form['batch']
    department = request.form['department']
<<<<<<< HEAD
    rank_id = request.form['rank']
    check_name = db.session.query(Student).filter_by(name=name).first()
    check_roll = db.session.query(Student).filter_by(roll_number=roll).first()
    if check_name is None and check_roll is None:
        student = Student(name, roll, gender, user, batch, department, rank_id)
=======
    rank = request.form['rank']
    student = Student(name, roll, gender, user, batch, department, rank)
    check_name = db.session.query(Student).filter_by(name=name).first()
    check_roll = db.session.query(Student).filter_by(roll_number=roll).first()
    if check_name is None and check_roll is None:
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        db.session.add(student)
        db.session.commit()
        flash('New student created')
        return redirect(url_for('student_blueprint.create_student'))
    else:
<<<<<<< HEAD
=======
        
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        if check_name is None:
            error = "Duplicate roll number!"
        elif check_roll is None:
            error = check_name, "already exists!"
        else:
<<<<<<< HEAD
            error = "Both name and roll number already exist!"
=======
            error = "Both name and roll number alreay exist!"
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        return render_template('/create_student.html', error=error, student_form=student_form)
    # return jsonify('success')


@blueprint.route('/<student_id>', methods=['GET', 'POST'])
@login_required
def update_student(student_id):
<<<<<<< HEAD
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    form = CreateStudentForm(request.form)
    student = Student.query.filter_by(id=student_id).first()
    if request.method == 'GET':
        return render_template('/update_student.html', form=form, student=student)
    elif request.method == 'DELETE':
        db.session.remove(student)
    else:
        name = request.form['name']
        gender = request.form['gender']
        roll_number = request.form['roll_number']
        user = request.form['user']
        batch = request.form['batch']
        department = request.form['department']
<<<<<<< HEAD
=======
        rank = request.form['rank']
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        student.name = name
        student.roll_number = roll_number
        student.gender = gender
        student.user_id = user
        student.batch_id = batch
        student.department_id = department
<<<<<<< HEAD
        student.rank_id = request.form['rank']
=======
        student.rank_id = rank
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        db.session.merge(student)
    db.session.commit()
    flash('Student updated')
    return redirect('students')
<<<<<<< HEAD


@blueprint.route('/summaries')
@login_required
def get_summaries():
    if current_user.roles[0].name == 'ADMIN':
        summaries = StudentSummary.query.all()
        return render_template('student_summary.html', summaries=summaries)
    if current_user.roles[0].name == 'USER':
        summaries = current_user.student.summaries
        return render_template('student_summary.html', summaries=summaries)


@blueprint.route('/summary/delete<summary_id>')
@login_required
def delete_summary(summary_id):
    if current_user.roles[0].name != 'ADMIN':
        return render_template('errors/page_403.html'), 403
    try:
        db.session.query(StudentSummary).filter_by(id=summary_id).delete()
        db.session.commit()
        flash('Summary deleted.')
        return redirect('/student/summaries')
    except Exception as e:
        print(e)
        flash('Delete error!')
        return redirect('/student/summaries')


## Errors
@blueprint.errorhandler(403)
def access_forbidden():
=======
    

## Errors
@blueprint.errorhandler(403)
def access_forbidden(error):
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
<<<<<<< HEAD
def not_found_error():
=======
def not_found_error(error):
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500
