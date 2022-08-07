from db import models
from core import teacher_view
from lib import common
logger1 = common.get_logger('讲师业务')

def login_interface(teacher_name, pwd):
    # 判断讲师是否登录
    if teacher_name == teacher_view.user_status.get('name'):
        return False, f'讲师{teacher_name}已登录,无需重复登录'
    # 判断讲师是否存在
    teacher_obj = models.Teacher.check_obj(teacher_name)
    if not teacher_obj:
        return False, '该讲师不存在,请联系管理员'
    # 判断密码是否正确，如果正确返回登录成功
    if pwd != teacher_obj.pwd:
        return False, f'讲师{teacher_name}密码错误'
    teacher_view.user_status['name'] = teacher_name
    logger1.info(f'讲师{teacher_name}登录成功')
    return True, f'讲师{teacher_name}登录成功'

def check_course_list_interface():
    return models.Course.check_all_obj()

def choice_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.check_obj(teacher_name)
    if course_name in teacher_obj.teach_course_list:
        return False, f'你已经选过课程{course_name},无需重复选择该课程'
    teacher_obj.teach_course_list.append(course_name)
    teacher_obj.save_obj()
    logger1.info(f'讲师{teacher_name}成功选择了课程:{course_name}')
    return True, f'讲师{teacher_name}成功选择了课程:{course_name}'

def check_teach_course_interface(teacher_name):
    teacher_obj = models.Teacher.check_obj(teacher_name)
    if not teacher_obj.teach_course_list:
        return False,'讲师暂未选择课程，请先选择课程'
    logger1.info(f'讲师{teacher_name}查看了教授课程')
    return True,teacher_obj.teach_course_list

def check_course_student_interface(course_name,teacher_name):
    course_obj = models.Course.check_obj(course_name)
    if not course_obj.course_student_list:
        return False,'暂无学生选择该课程'
    logger1.info(f'讲师{teacher_name}查看了课程学生')
    return True,course_obj.course_student_list

def update_course_score_interface(course_student_name,update_score,target_course_name,teacher_name):
    student_obj = models.Student.check_obj(course_student_name)
    student_obj.score[target_course_name]=update_score
    student_obj.save_obj()
    course_obj = models.Course.check_obj(target_course_name)
    course_obj.course_score_dict[course_student_name] = {target_course_name:update_score}
    course_obj.save_obj()
    logger1.info(f'讲师{teacher_name}成功修改了学生:{course_student_name}的课程:{target_course_name}的分数')
    return True, f'讲师{teacher_name}成功修改了学生:{course_student_name}的课程:{target_course_name}的分数'
