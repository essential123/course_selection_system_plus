from core import admin_view, student_view, teacher_view

view_dict = {
    '1': admin_view,
    '2': student_view,
    '3': teacher_view
}


def run():
    while True:
        print('''
        ----------------总试图-----------------
        1.管理员视图
        2.学生视图
        3.老师视图
        --------------------------------------
        ''')

        view_id = input('请输入你想要操作的视图编号(输入q退出)>>:').strip()
        if view_id == 'q':
            break
        elif view_id in view_dict:
            view_name = view_dict[view_id]
            view_name.run()
        else:
            print('输入超出范围')
