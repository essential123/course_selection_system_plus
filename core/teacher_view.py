from interface import teacher_interface
from lib import common

user_status = {
    'name': ''
}


def login():
    teacher_name = input('请输入您的用户名>>:').strip()
    pwd = input('请输入您的密码>>:').strip()
    if teacher_name and pwd:
        pwd = int(pwd)
        flag, msg = teacher_interface.login_interface(teacher_name, pwd)
        print(msg)
    else:
        print('输入不能为空')


@common.auth_user('teacher')
def choice_teach_course():
    course_list = teacher_interface.check_course_list_interface()
    if not course_list:
        print('当前暂无课程可供选择')
        return
    for course_id, course_name in enumerate(course_list, start=1):
        print(f'{course_id},{course_name}')
    target_course_id = input('请输入您想要的选择课程编号（输入q或者空退出）>>:').strip()
    if target_course_id == 'q' or target_course_id == '':
        return
    target_course_id = int(target_course_id)
    if target_course_id not in range(1, len(course_list) + 1):
        print('输入的课程编号不存在')
        return
    target_course_name = course_list[target_course_id - 1]
    flag, msg = teacher_interface.choice_course_interface(target_course_name, user_status.get('name'))
    print(msg)


@common.auth_user('teacher')
def check_teach_course():
    flag, course_list = teacher_interface.check_teach_course_interface(user_status.get('name'))
    if not flag:
        print(course_list)
        return
    for course_id, course_name in enumerate(course_list, start=1):
        print(f'{course_id},{course_name}')


@common.auth_user('teacher')
def check_course_student():
    flag, course_list = teacher_interface.check_teach_course_interface(user_status.get('name'))
    if not flag:
        print(course_list)
        return
    for course_id, course_name in enumerate(course_list, start=1):
        print(f'{course_id},{course_name}')
    target_course_id = input('请输入您想要查看的课程编号（输入q或者空退出）>>:').strip()
    if target_course_id == 'q' or target_course_id == '':
        return
    target_course_id = int(target_course_id)
    if target_course_id not in range(1, len(course_list) + 1):
        print('输入的课程编号不存在')
        return
    target_course_name = course_list[target_course_id - 1]
    flag, course_student_list = teacher_interface.check_course_student_interface(target_course_name,user_status.get('name'))
    print(course_student_list)


@common.auth_user('teacher')
def update_course_score():
    flag, course_list = teacher_interface.check_teach_course_interface(user_status.get('name'))
    if not flag:
        print(course_list)
        return
    for course_id, course_name in enumerate(course_list, start=1):
        print(f'{course_id},{course_name}')
    target_course_id = input('请输入您想要查看的课程编号（输入q或者空退出）>>:').strip()
    if target_course_id == 'q' or target_course_id == '':
        return
    target_course_id = int(target_course_id)
    if target_course_id not in range(1, len(course_list) + 1):
        print('输入的课程编号不存在')
        return
    target_course_name = course_list[target_course_id - 1]
    flag, course_student_list = teacher_interface.check_course_student_interface(target_course_name)
    if not flag:
        print(course_student_list)
        return
    for course_student_id, course_student_name in enumerate(course_student_list, start=1):
        print(f'{course_student_id},{course_student_name}')
    course_student_id = input('请输入您想要修改成绩的学生编号（输入q或者空退出）>>:').strip()
    update_score = input('请输入该学生的分数>>:').strip()
    if update_score == '':
        print('输入不能为空')
        return
    if course_student_id == 'q' or course_student_id == '':
        return
    course_student_id = int(course_student_id)
    if course_student_id not in range(1, len(course_student_list) + 1):
        print('输入的学生编号不存在')
        return
    course_student_name = course_student_list[course_student_id - 1]
    flag, msg = teacher_interface.update_course_score_interface(course_student_name, update_score, target_course_name,
                                                                user_status.get('name'))
    print(msg)


func_dict = {
    '1': login,
    '2': choice_teach_course,
    '3': check_teach_course,
    '4': check_course_student,
    '5': update_course_score
}


def run():
    while True:
        print('''
        ----------------讲师视图------------------
        1.讲师登录功能
        2.讲师选择教授的课程
        3.讲师查看教授课程
        4.讲师查看课程学生
        5.讲师管理学生课程分数
        -----------------------------------------
        ''')

        func_id = input('请输入你想要执行的功能编号(输入q退出)>>:').strip()
        if func_id == 'q':
            break
        elif func_id in func_dict:
            view_name = func_dict[func_id]
            view_name()
        else:
            print('输入超出范围')
