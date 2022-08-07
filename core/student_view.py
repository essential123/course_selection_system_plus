from interface import student_interface
from lib import common
user_status = {
    'name': ''
}

def register():
    # 获取学生姓名
    student_name = input('请输入您的用户名>>:').strip()
    if student_name:
        flag, msg = student_interface.register_interface(student_name)
        print(msg)
    else:
        print('用户名输入不能为空')


def login():
    student_name = input('请输入您的用户名>>:').strip()
    pwd = input('请输入您的密码>>:').strip()
    if student_name and pwd:
        flag, msg = student_interface.login_interface(student_name, pwd)
        print(msg)
    else:
        print('输入不能为空')

@common.auth_user('student')
def choice_school():
    school_list = student_interface.get_all_school_interface()
    if not school_list:
        print('暂无学校可供选择')
        return
    for school_id, school_name in enumerate(school_list, start=1):
        print(f'{school_id},{school_name}')
    target_school_id = input('请输入您想要的选择的学校编号>>:').strip()
    if target_school_id == 'q' or target_school_id == '':
        return
    target_school_id = int(target_school_id)
    if target_school_id not in range(1, len(school_list) + 1):
        print('输入的学校编号不存在')
        return
    target_school_name = school_list[target_school_id - 1]
    flag, msg = student_interface.choice_school_interface(target_school_name,user_status.get('name'))
    print(msg)


@common.auth_user('student')
def choice_course():
    flag, course_list = student_interface.check_course_list_interface(user_status.get('name'))
    if not flag:
        print(course_list)
    if not course_list:
        print('当前暂无课程可供选择')
        return
    for course_id, course_name in enumerate(course_list, start=1):
        print(f'{course_id},{course_name}')
    target_course_id = input('请输入您想要的选择课程编号>>:').strip()
    if target_course_id == 'q' or target_course_id == '':
        return
    target_course_id = int(target_course_id)
    if target_course_id not in range(1, len(course_list) + 1):
        print('输入的课程编号不存在')
        return
    target_course_name = course_list[target_course_id - 1]
    flag, msg = student_interface.choice_course_interface(target_course_name,user_status.get('name'))
    print(msg)


@common.auth_user('student')
def check_score():
    course_list = student_interface.get_all_course_interface(user_status.get('name'))
    if not course_list:
        print('暂无报名任何课程,请先报名课程')
        return
    for course_id, course_name in enumerate(course_list, start=1):
        print(f'{course_id},{course_name}')
    target_course_id = input('请输入您想要的查询的课程编号>>:').strip()
    if target_course_id == 'q' or target_course_id == '':
        return
    target_course_id = int(target_course_id)
    if target_course_id not in range(1, len(course_list) + 1):
        print('输入的课程编号不存在')
        return
    target_course_name = course_list[target_course_id - 1]
    flag, msg = student_interface.check_score_interface(target_course_name,user_status.get('name'))
    print(msg)

func_dict = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score
}


def run():
    while True:
        print('''
        ----------------管理员试图-----------------
        1.学生注册功能
        2.学生登录功能
        3.学生选择学校
        4.学生选择课程
        5.学生查看分数
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
