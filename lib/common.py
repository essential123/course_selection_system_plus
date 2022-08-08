import logging.config
from conf import settings
def auth_user(role):
    def outter(func):
        def inner(*args,**kwargs):
            from core import admin_view,student_view,teacher_view
            role_dict = {
                'admin': admin_view,
                'student': student_view,
                'teacher': teacher_view
            }
            if role not in role_dict:
                print('没有该视图')
                return
            view_name = role_dict[role]
            if view_name.user_status.get('name'):
                res = func(*args,**kwargs)
                return res
            else:
                print('您暂未登录,无法执行该功能，请先登录')
                view_name.login()
        return inner
    return outter

def get_logger(title):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger1 = logging.getLogger(title)
    return logger1