from sqlalchemy import Column, Integer, String, Float
from app import db
<<<<<<< HEAD
from app.project.models import ProjectMembers
=======
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484


class Student(db.Model):
    __tablename__ = 'student'
<<<<<<< HEAD
    id = Column(Integer, primary_key=True, autoincrement=True)
=======
    id = Column(Integer, primary_key=True)
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    name = Column(String, unique=True)
    roll_number = Column(String, unique=True)
    gender = Column(String)
    user_id = db.Column(Integer, db.ForeignKey('user.id'))
    batch_id = db.Column(Integer, db.ForeignKey('batch.id'))
    department_id = db.Column(Integer, db.ForeignKey('department.id'))
    rank_id = db.Column(Integer, db.ForeignKey('rank.id'))
<<<<<<< HEAD
    created_at = Column(db.DateTime, nullable=True)
    updated_at = Column(db.DateTime, nullable=True)
    reports = db.relationship('Report', backref='student', lazy=True)
    tasks = db.relationship('Task', backref='student', lazy=True)
    summaries = db.relationship('StudentSummary', backref='student', lazy=True)
    # projects = db.relationship('Project',
    #                           secondary=ProjectMembers,
    #                           lazy='dynamic',
    #                           backref=db.backref('students', lazy='dynamic'))

=======
    created_at = Column(String(50), nullable=True)
    updated_at = Column(String(50), nullable=True)
  
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    def __init__(self, name, roll_number, gender, user_id, batch_id, department_id, rank_id):
        self.name = name
        self.roll_number = roll_number
        self.gender = gender
        self.user_id = user_id
        self.batch_id = batch_id
        self.department_id = department_id
        self.rank_id = rank_id
<<<<<<< HEAD

    def __repr__(self):
        return str(self.name)


class Rank(db.Model):
    __tablename__ = 'rank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(15), unique=True)
    code = Column(String(5), unique=True)
    description = Column(String(100))
    students = db.relationship('Student', uselist=False, backref='rank', lazy=True)
    chargeTable = db.relationship('ChargeTable', uselist=False, backref='rank', lazy=True)
    created_at = Column(db.DateTime, nullable=True)
    updated_at = Column(db.DateTime, nullable=True)

=======
  
    def __repr__(self):
        return str(self.name)
    

class Rank(db.Model):
    __tablename__ = 'rank'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), unique=True)
    code = Column(String(5), unique=True)
    description = Column(String(100))
    students = db.relationship('Student', backref='rank', lazy=True)
    chargeTables = db.relationship('ChargeTable', backref='rank', lazy=True)
    created_at = Column(String(50), nullable=True)
    updated_at = Column(String(50), nullable=True)
    
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    def __init__(self, name, code, description):
        self.name = name
        self.code = code
        self.description = description
<<<<<<< HEAD

    def __repr__(self):
        return str(self.name)


class ChargeTable(db.Model):
    __tablename__ = 'charge_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float(2, True, 2), default=0.00)
=======
        
    def __repr__(self):
        return str(self.name)
    
    
class ChargeTable(db.Model):
    __tablename__ = 'charge_table'
    id = Column(Integer, primary_key=True)
    price = Column(Float(3, True, 3))
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    department_id = db.Column(Integer, db.ForeignKey('department.id'))
    batch_id = db.Column(Integer, db.ForeignKey('batch.id'))
    semester_id = db.Column(Integer, db.ForeignKey('semester.id'))
    rank_id = db.Column(Integer, db.ForeignKey('rank.id'))
<<<<<<< HEAD
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)

=======
    created_at = Column(String(50))
    updated_at = Column(String(50))
    
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
    def __init__(self, price, department_id, batch_id, semester_id, rank_id):
        self.price = price
        self.department_id = department_id
        self.batch_id = batch_id
        self.semester_id = semester_id
        self.rank_id = rank_id
<<<<<<< HEAD

    def __repr__(self):
        return str(self.price)


class StudentSummary(db.Model):
    __tablename__ = 'student_summary'
    id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = db.Column(Integer, db.ForeignKey('department.id'))
    batch_id = db.Column(Integer, db.ForeignKey('batch.id'))
    semester_id = db.Column(Integer, db.ForeignKey('semester.id'))
    student_id = db.Column(Integer, db.ForeignKey('student.id'))
    project_id = db.Column(Integer, db.ForeignKey('project.id'))
    planning_hour = Column(Float(2, True, 2), default=0.00)
    actual_hour = Column(Float(2, True, 2), default=0.00)
    actual_point = Column(Float(2, True, 2), default=0.00)
    estimate_point = Column(Float(2, True, 2), default=0.00)
    propose_point = Column(Float(2, True, 2), default=0.00)
    acquire_point = Column(Float(2, True, 2), default=0.00)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)

    def __init__(self, department, batch, semester, student, project, planning_hour,
                 actual_hour, actual_point, estimate_point, propose_point, acquire_point):
        self.department_id = department
        self.batch_id = batch
        self.semester_id = semester
        self.student_id = student
        self.project_id = project
        self.planning_hour = planning_hour
        self.actual_hour = actual_hour
        self.actual_point = actual_point
        self.estimate_point = estimate_point
        self.propose_point = propose_point
        self.acquire_point = acquire_point

    def __repr__(self):
        return str(self.semester_id)

=======
        
    def __repr__(self):
        return self.price
>>>>>>> ed04d2fc84a43bdd8f4a7a76e3e197d11f693484
