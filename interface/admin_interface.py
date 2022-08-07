from db import models
from core import admin_view
from lib import common
logger1 = common.get_logger('管理员业务')

def register_interface(admin_name):
    # 判断管理员是否存在
    admin_obj = models.Admin.check_obj(admin_name)
    if admin_obj:
        return False, f'管理员{admin_name}已注册，无需重复注册'
    # 获取管理员密码，完成管理员注册功能
    pwd = input('请输入您的密码>>:').strip()
    if not pwd:
        return False, '密码不能为空'
    pwd_twice = input('请再次输入您的密码>>:').strip()
    if pwd != pwd_twice:
        return False, '两次密码输入不一致'
    models.Admin(admin_name, pwd)
    logger1.info(f'管理员{admin_name}注册成功')
    return True, f'管理员{admin_name}注册成功'


def login_interface(admin_name, pwd):
    # 判断管理员是否登录
    if admin_name == admin_view.user_status.get('name'):
        return False, f'管理员{admin_name}已登录,无需重复登录'
    # 判断管理员是否存在
    admin_obj = models.Admin.check_obj(admin_name)
    if not admin_obj:
        return False, '该管理员不存在,请先注册'
    # 判断密码是否正确，如果正确返回登录成功
    if pwd != admin_obj.pwd:
        return False, f'管理员{admin_name}密码错误'
    admin_view.user_status['name'] = admin_name
    logger1.info(f'管理员{admin_name}登录成功')
    return True, f'管理员{admin_name}登录成功'


def create_school_interface(school_name, school_address, admin_name):
    school_obj = models.School.check_obj(school_name)
    if school_obj:
        return False, f'当前学校{school_name}已存在,无需重复创建该学校'
    admin_obj = models.Admin.check_obj(admin_name)
    admin_obj.create_school(school_name, school_address)
    logger1.info(f'管理员:{admin_name}创建了{school_name},地点在:{school_address}')
    return True, f'管理员:{admin_name}创建了{school_name},地点在:{school_address}'


def get_all_school_interface():
    return models.School.check_all_obj()


def create_course_interface(school_name, course_name, course_price, course_period, admin_name):
    school_obj = models.School.check_obj(school_name)
    if course_name in school_obj.course_list:
        return False, f'当前课程{course_name}已存在,无需重复创建该课程'
    admin_obj = models.Admin.check_obj(admin_name)
    admin_obj.create_course(school_name, course_name, course_price, course_period)
    school_obj.course_list.append(course_name)
    models.School.save_obj(school_obj)
    logger1.info(f'管理员:{admin_name},在学校:{school_name},创建了{course_name}课程')
    return True, f'管理员:{admin_name},在学校:{school_name},创建了{course_name}课程'


def create_teacher_interface(teacher_name, admin_name):
    teacher_obj = models.Teacher.check_obj(teacher_name)
    if teacher_obj:
        return False, f'当前讲师{teacher_name}已存在,无需重复创建该讲师'
    admin_obj = models.Admin.check_obj(admin_name)
    admin_obj.create_teacher(teacher_name)
    logger1.info(f'管理员:{admin_name},创建了讲师:{teacher_name}')
    return True, f'管理员:{admin_name},创建了讲师:{teacher_name}'
