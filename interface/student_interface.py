from db import models
from core import student_view
from lib import common
logger1 = common.get_logger('学生业务')

def register_interface(student_name):
    # 判断学生是否存在
    student_obj = models.Student.check_obj(student_name)
    if student_obj:
        return False, f'管理员{student_name}已注册，无需重复注册'
    # 获取学生密码，完成学生注册功能
    pwd = input('请输入您的密码>>:').strip()
    if not pwd:
        return False, '密码不能为空'
    pwd_twice = input('请再次输入您的密码>>:').strip()
    if pwd != pwd_twice:
        return False, '两次密码输入不一致'
    models.Student(student_name, pwd)
    logger1.info(f'管理员{student_name}注册成功')
    return True, f'管理员{student_name}注册成功'


def login_interface(student_name, pwd):
    # 判断学生是否登录
    if student_name == student_view.user_status.get('name'):
        return False, f'学生{student_name}已登录,无需重复登录'
    # 判断学生是否存在
    student_obj = models.Student.check_obj(student_name)
    if not student_obj:
        return False, '该学生不存在,请先注册'
    # 判断密码是否正确，如果正确返回登录成功
    if pwd != student_obj.pwd:
        return False, f'学生{student_name}密码错误'
    student_view.user_status['name'] = student_name
    logger1.info(f'学生{student_name}登录成功')
    return True, f'学生{student_name}登录成功'


def get_all_school_interface():
    return models.School.check_all_obj()


def choice_school_interface(school_name, student_name):
    student_obj = models.Student.check_obj(student_name)
    if student_obj.school_name:
        return False, f'{student_name}已经选择了{school_name},无需再次选择'
    student_obj.school_name = school_name
    student_obj.save_obj()
    logger1.info(f'学生{student_name}成功选择学校:{school_name},欢迎你成为{school_name}的一员')
    return True, f'学生{student_name}成功选择学校:{school_name},欢迎你成为{school_name}的一员'


def check_course_list_interface(student_name):
    student_obj = models.Student.check_obj(student_name)
    school_obj = models.School.check_obj(student_obj.school_name)
    if not student_obj.school_name:
        return False, f'学生{student_name}暂未选择学校,请先选择学校'
    return True, school_obj.course_list


def choice_course_interface(course_name, student_name):
    student_obj = models.Student.check_obj(student_name)
    if course_name in student_obj.course_list:
        return False, f'你已经选过课程{course_name},无需重复选择该课程'
    student_obj.course_list.append(course_name)
    student_obj.score[course_name] = '该课程暂无考核'
    student_obj.save_obj()
    course_obj = models.Course.check_obj(course_name)
    course_obj.course_student_list.append(student_name)
    course_obj.course_score_dict[student_name] = {course_name:'该课程暂无考核'}
    course_obj.save_obj()
    logger1.info(f'学生{student_name}成功选择了课程:{course_name}')
    return True, f'学生{student_name}成功选择了课程:{course_name}'


def get_all_course_interface(student_name):
    student_obj = models.Student.check_obj(student_name)
    return student_obj.course_list


def check_score_interface(course_name, student_name):
    student_obj = models.Student.check_obj(student_name)
    if course_name in student_obj.course_list:
        logger1.info(f'学生{student_name}查看了{course_name}分数')
        return True, student_obj.score.get(course_name)
