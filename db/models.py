from db import db_handler


class Base(object):
    def save_obj(self):
        db_handler.save_obj(self)

    @classmethod
    def check_obj(cls, name):
        return db_handler.check_obj(cls, name)

    @classmethod
    def check_all_obj(cls):
        return db_handler.check_all_obj(cls)


class Admin(Base):
    def __init__(self, admin_name, pwd):
        self.name = admin_name
        self.pwd = pwd
        self.save_obj()

    def create_school(self, school_name, school_address):
        return School(school_name, school_address)

    def create_course(self, school_name, course_name, course_price, course_period):
        return Course(school_name, course_name, course_price, course_period)

    def create_teacher(self, teacher_name):
        return Teacher(teacher_name)


class School(Base):
    def __init__(self, school_name, school_address):
        self.name = school_name
        self.school_address = school_address
        self.course_list = []
        self.save_obj()


class Course(Base):
    def __init__(self, school_name, course_name, course_price, course_period):
        self.name = course_name
        self.course_school = school_name
        self.course_price = course_price
        self.course_period = course_period
        self.course_student_list = []
        self.course_score_dict = {}
        self.save_obj()


class Teacher(Base):
    def __init__(self, teacher_name, pwd=123):
        self.name = teacher_name
        self.pwd = pwd
        self.teach_course_list = []
        self.save_obj()


class Student(Base):
    def __init__(self, student_name, pwd):
        self.name = student_name
        self.pwd = pwd
        self.school_name = None
        self.course_list = []
        self.score = {}
        self.save_obj()
