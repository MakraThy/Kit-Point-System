<<<<<<< HEAD
from bcrypt import checkpw, gensalt, hashpw
=======
from bcrypt import checkpw
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
from datetime import datetime
from flask import jsonify, render_template, redirect, request, url_for, flash, json, Response
from flask_login import (
  current_user,
  login_required,
  login_user,
  logout_user
)

from app import db, login_manager
from app.base import blueprint
<<<<<<< HEAD
from app.base.forms import LoginForm, CreateAccountForm, CreateDepartmentForm, \
  CreateBatchForm, CreateSemesterForm, CreateRoleForm
from app.base.models import User, Role, Department, Batch, Semester, KitPointValue, AverageInternHour
=======
from app.base.forms import LoginForm, CreateAccountForm, CreateDepartmentForm, CreateBatchForm, CreateSemesterForm
from app.base.models import User, Role, Department, Batch, Semester
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484


@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


<<<<<<< HEAD
# @blueprint.route('/<template>')
# @login_required
# def route_template(template):
#     return render_template(template + '.html')
=======
@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484


@blueprint.route('/fixed_<template>')
@login_required
def route_fixed_template(template):
    return render_template('fixed/fixed_{}.html'.format(template))


@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))


<<<<<<< HEAD
@blueprint.route('/kit/point/values')
@login_required
def get_kit_point_value():
    return render_template('list/kit_point_value.html', kit_point=KitPointValue.query.all())


@blueprint.route('/kit/point/value/create', methods=['POST'])
@login_required
def create_kit_point_value():
    check = KitPointValue.query.all()
    if len(check) == 0:
        value = request.form.get('value')
        if int(value) <= 0:
            flash('Not allowed!')
        else:
            kit_point = KitPointValue(value)
            kit_point.created_at = datetime.today()
            db.session.add(kit_point)
            db.session.commit()
            flash('Point value created')
    else:
        flash('Point allowed to creat only once!')
    return redirect('/kit/point/values')


@blueprint.route('/kit/point/value/<point_id>', methods=['POST', 'GET'])
@login_required
def update_kit_point_value(point_id):
    point_value = KitPointValue.query.filter_by(id=point_id).first()
    if request.method == 'GET':
        return jsonify(
          {
            'id': point_value.id,
            'value': point_value.value
          }
        )
    else:
        point_value.value = request.form.get('value')
        point_value.updated_at = datetime.today()
        db.session.merge(point_value)
        db.session.commit()
        flash('Point value updated')
        return jsonify('success')


@blueprint.route('/kit/point/value/delete<point_id>')
@login_required
def delete_kit_point_value(point_id):
    try:
        KitPointValue.query.filter_by(id=point_id).delete()
        db.session.commit()
        flash('Value deleted')
        return redirect('/kit/point/values')
    except Exception as e:
        print(e)
        flash('Delete error! some entities are referring to this')
        return redirect('/kit/point/values')


## Login & Registration
@blueprint.route('/role/create', methods=['POST'])
@login_required
def create_role():
    name = request.form.get('name')
    role = Role(name)
    db.session.add(role)
    db.session.commit()
    flash('Role created')
    return redirect('/create_user')


@blueprint.route('/delete<user_id>')
@login_required
def delete_user(user_id):
    try:
        User.query(User).filter_by(id=user_id).delete()
        db.session.commit()
        flash('User deleted')
        return redirect('/users')
    except Exception as e:
        print(e)
        flash('Delete error! some entities are referring to this')
        return redirect('/users')


@blueprint.route('/<user_id>', methods=['GET', 'POST'])
@login_required
def update_user(user_id):
    user = db.session.query(User).get(user_id)
    if request.method == 'GET':
        form = CreateAccountForm(request.form)
        roleForm = CreateRoleForm(request.form)
        return render_template('form/update_user.html', form=form, user=user, roleForm=roleForm)
    else:
        user.email = request.form.get('email')
        user.username = request.form.get('username')
        user.password = hashpw(request.form.get('password').encode('utf8'), gensalt())
        role = db.session.query(Role).get(request.form.get('role'))
        user.roles.remove(user.roles[0])
        user.roles.append(role)
        db.session.merge(user)
        db.session.commit()
        flash('User updated')
        return redirect('/users')
=======
## Login & Registration
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and checkpw(password.encode('utf8'), user.password):
            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))
        return render_template('errors/page_403.html')
    if not current_user.is_authenticated:
        return render_template(
          'login/login.html',
          login_form=login_form,
          create_account_form=create_account_form
        )
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        userForm = CreateAccountForm(request.form)
<<<<<<< HEAD
        roleform = CreateRoleForm(request.form)
        return render_template('form/create_user.html', userForm=userForm, roleForm=roleform)
    email = request.form['email']
    username = request.form['username']
=======
        return render_template('form/create_user.html', userForm=userForm)
    email = request.form['email']
    username = request.form['username']
    print(username)
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    check_email = db.session.query(User).filter_by(email=email).first()
    check_username = db.session.query(User).filter_by(username=username).first()
    if '@kit.edu.kh' in email:
        print('yeeeeeeeeeeeeeeee')
    else:
        print('noooooooooooooooooo')
    if check_email is None and check_username is None:
<<<<<<< HEAD

        role = db.session.query(Role).get(request.form.get('role'))
        user = User(**request.form)
        print(user.username)
=======
        role = db.session.query(Role).get(2)
        user = User(**request.form)
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        # user.roles.append(Role('ADMIN'))
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        return jsonify('success')
    else:
        return jsonify('duplicate')


<<<<<<< HEAD
@blueprint.route('/department/<department_id>', methods=['GET', 'POST'])
@login_required
def update_department(department_id):
    form = CreateDepartmentForm(request.form)
    department = Department.query.filter_by(id=department_id).first()
    if request.method == 'GET':
        return render_template('/form/update_department.html', departmentForm=form, department=department)
    else:
        department.name = request.form.get('name')
        department.code = request.form.get('code')
        department.updated_at = datetime.now()
        db.session.merge(department)
        db.session.commit()
        flash('Department updated')
        return redirect('/departments')


@blueprint.route('/batch/<batch_id>', methods=['GET', 'POST'])
@login_required
def update_batch(batch_id):
    form = CreateBatchForm(request.form)
    batch = Batch.query.filter_by(id=batch_id).first()
    if request.method == 'GET':
        return render_template('/form/update_batch.html', batchForm=form, batch=batch)
    else:
        batch.name = request.form.get('name')
        batch.code = request.form.get('code')
        batch.department_id = request.form.get('department')
        batch.start_date = request.form.get('start_date')
        batch.end_date = request.form.get('end_date')
        batch.updated_at = datetime.now()
        db.session.merge(batch)
        db.session.commit()
        flash('Batch updated')
        return redirect('/batches')


@blueprint.route('/semester/<semester_id>', methods=['GET', 'POST'])
@login_required
def update_semester(semester_id):
    global year_id
    form = CreateSemesterForm(request.form)
    semester = Semester.query.filter_by(id=semester_id).first()
    if request.method == 'GET':
        return render_template('/form/update_semester.html', semesterForm=form, semester=semester)
    else:
        name = request.form.get('name')
        if '1' in name or '2' in name:
            year_id = AverageInternHour.query.get(1).id
        elif '3' in name or '4' in name:
            year_id = AverageInternHour.query.get(2).id
        elif '5' in name or '6' in name:
            year_id = AverageInternHour.query.get(3).id
        elif '7' in name or '8' in name:
            year_id = AverageInternHour.query.get(4).id
        semester.name = name
        semester.code = request.form.get('code')
        semester.department_id = request.form.get('department')
        semester.year_id = year_id
        semester.start_date = request.form.get('start_date')
        semester.end_date = request.form.get('end_date')
        semester.updated_at = datetime.now()
        db.session.merge(semester)
        db.session.commit()
        flash('Semester updated')
        return redirect('/semesters')


@blueprint.route('/department/delete<department_id>')
@login_required
def delete_department(department_id):
    try:
        Department.query.filter_by(id=department_id).delete()
        db.session.commit()
        flash('Department deleted!')
        return redirect('/departments')
    except Exception as e:
        print(e)
        flash("Delete error!, can't delete. Some entities are referring to it!")
        return redirect('/departments')


@blueprint.route('/batch/delete<batch_id>')
@login_required
def delete_batch(batch_id):
    try:
        Batch.query.filter_by(id=batch_id).delete()
        db.session.commit()
        flash('Batch deleted!')
        return redirect('/batches')
    except Exception as e:
        print(e)
        flash("Delete error!, can't delete. Some entities are referring to it!")
        return redirect('/batches')


@blueprint.route('/semester/delete<semester_id>')
@login_required
def delete_semester(semester_id):
    try:
        Semester.query.filter_by(id=semester_id).delete()
        db.session.commit()
        flash('Batch deleted!')
        return redirect('/semesters')
    except Exception as e:
        print(e)
        flash("Delete error!, can't delete. Some entities are referring to it!")
        return redirect('/semesters')


@blueprint.route('/create_department', methods=['GET', 'POST'])
@login_required
=======
@blueprint.route('/create_department', methods=['GET', 'POST'])
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def create_department():
    if request.method == 'GET':
        departmentForm = CreateDepartmentForm(request.form)
        return render_template('form/create_department.html', departmentForm=departmentForm)
    name = request.form['name']
    code = request.form['code']
    check_name = db.session.query(Department).filter_by(name=name).first()
    if check_name is None:
        department = Department(name, code)
        department.created_at = datetime.now()
        db.session.add(department)
        db.session.commit()
        flash('New department created')
        return redirect(url_for('base_blueprint.create_department'))
    else:
        departmentForm = CreateDepartmentForm(request.form)
        error = "Duplicate entry!"
        return render_template('form/create_department.html', error=error, departmentForm=departmentForm)


@blueprint.route('/create_batch', methods=['GET', 'POST'])
<<<<<<< HEAD
@login_required
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def create_batch():
    if request.method == 'GET':
        batchForm = CreateBatchForm(request.form)
        return render_template('form/create_batch.html', batchForm=batchForm)
    name = request.form['name']
    code = request.form['code']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    department_id = request.form['department']
    check_code = db.session.query(Batch).filter_by(code=code).first()
    check_duplicate = db.session.query(Batch).filter_by(name=name, department_id=department_id).first()
    if check_code is None and check_duplicate is None:
        created_at = datetime.now()
        batch = Batch(name, code, start_date, end_date, department_id)
        batch.created_at = created_at
        db.session.add(batch)
        db.session.commit()
        flash('New batch created')
        return redirect(url_for('base_blueprint.create_batch'))
    else:
        batchForm = CreateBatchForm(request.form)
        error = "Duplicate entry!"
        return render_template('form/create_batch.html', error=error, batchForm=batchForm)


@blueprint.route('/create_semester', methods=['GET', 'POST'])
<<<<<<< HEAD
@login_required
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def create_semester():
    if request.method == 'GET':
        semesterForm = CreateSemesterForm(request.form)
        return render_template('form/create_semester.html', semesterForm=semesterForm)
    name = request.form['name']
    code = request.form['code']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    batch_id = request.form['batch']
    department_id = request.form['department']
    check_code = db.session.query(Semester).filter_by(code=code).first()
    check_duplicate = db.session.query(Semester).filter_by(name=name,
                                                           batch_id=batch_id,
                                                           department_id=department_id).first()
    if check_code is None and check_duplicate is None:
<<<<<<< HEAD
        if '1' in name or '2' in name:
            year_id = AverageInternHour.query.get(1).id
        elif '3' in name or '4' in name:
            year_id = AverageInternHour.query.get(2).id
        elif '5' in name or '6' in name:
            year_id = AverageInternHour.query.get(3).id
        elif '7' in name or '8' in name:
            year_id = AverageInternHour.query.get(4).id
        created_at = datetime.now()
        semester = Semester(name, code, start_date, end_date, batch_id, department_id, year_id)
=======
        created_at = datetime.now()
        semester = Semester(name, code, start_date, end_date, batch_id, department_id)
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
        semester.created_at = created_at
        db.session.add(semester)
        db.session.commit()
        flash('New semester created')
        return redirect(url_for('base_blueprint.create_semester'))
    else:
        semesterForm = CreateSemesterForm(request.form)
        error = "Duplicate entry!"
        return render_template('form/create_semester.html', error=error, semesterForm=semesterForm)


@blueprint.route('/departments')
<<<<<<< HEAD
@login_required
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def get_departments():
    departments = db.session.query(Department).all()
    return render_template('list/department.html', departments=departments)


@blueprint.route('/users')
<<<<<<< HEAD
@login_required
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def get_users():
    users = db.session.query(User).all()
    return render_template('list/user.html', users=users)


@blueprint.route('/batches')
<<<<<<< HEAD
@login_required
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def get_batches():
    batches = db.session.query(Batch).all()
    return render_template('list/batch.html', batches=batches)


@blueprint.route('/semesters')
<<<<<<< HEAD
@login_required
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
def get_semesters():
    semesters = db.session.query(Semester).all()
    return render_template('list/semester.html', semesters=semesters)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


## Errors
@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500
