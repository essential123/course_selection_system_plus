from interface import admin_interface
from lib import common

user_status = {
    'name': ''
}


def register():
    # 获取管理员姓名
    admin_name = input('请输入您的用户名>>:').strip()
    if admin_name:
        flag, msg = admin_interface.register_interface(admin_name)
        print(msg)
    else:
        print('用户名输入不能为空')


def login():
    admin_name = input('请输入您的用户名>>:').strip()
    pwd = input('请输入您的密码>>:').strip()
    flag, msg = admin_interface.login_interface(admin_name, pwd)
    print(msg)


@common.auth_user('admin')
def create_school():
    school_name = input('请输入您想要创建的学校名称>>:').strip()
    school_address = input('请输入您想要创建的学校地址>>:').strip()
    if school_name and school_address:
        flag, msg = admin_interface.create_school_interface(school_name, school_address, user_status.get('name'))
        print(msg)
    else:
        print('输入不能为空')


@common.auth_user('admin')
def create_course():
    school_list = admin_interface.get_all_school_interface()
    if not school_list:
        print('暂无学校,请先创建学校')
        return
    for school_id, school_name in enumerate(school_list, start=1):
        print(f'{school_id},{school_name}')
    target_school_id = input('请输入您想要的创建课程的学校编号（输入q或者空退出）>>:').strip()
    if target_school_id == 'q' or target_school_id == '':
        return
    target_school_id = int(target_school_id)
    if target_school_id not in range(1, len(school_list) + 1):
        print('输入的学校编号不存在')
        return
    target_school_name = school_list[target_school_id - 1]
    course_name = input('请输入您想要创建的课程名称（输入q或者空退出）>>:').strip()
    course_name = f'{target_school_name}_{course_name}'
    course_price = input('请输入您创建的课程的价格>>:').strip()
    course_period = input('请输入您创建的课程的周期>>:').strip()
    if course_name and course_price and course_period:
        flag, msg = admin_interface.create_course_interface(target_school_name, course_name, course_price, course_period,
                                                            user_status.get('name'))
        print(msg)
    else:
        print('输入不能为空')


@common.auth_user('admin')
def create_teacher():
    teacher_name = input('请输入您创建的老师名称>>:').strip()
    if teacher_name:
        flag, msg = admin_interface.create_teacher_interface(teacher_name, user_status.get('name'))
        print(msg)
    else:
        print('输入不能为空')

func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher
}


def run():
    while True:
        print('''
        ----------------管理员试图-----------------
        1.管理员注册功能
        2.管理员登录功能
        3.管理员创建学校
        4.管理员创建课程
        5.管理员创建讲师
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
