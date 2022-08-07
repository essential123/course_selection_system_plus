import os

from conf import settings
import pickle


def save_obj(obj):
    # 拼接路径，判断文件夹路径是否存在，如果不存在创建该路径的文件夹
    folder_path = os.path.join(settings.DB_PATH, obj.__class__.__name__)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    # 拼接对象路径，将信息写入文件
    file_path = os.path.join(folder_path, obj.name)
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)


def check_obj(cls, name):
    # 拼接路径，判断文件夹路径是否存在，如果不存在创建该路径的文件夹
    folder_path = os.path.join(settings.DB_PATH, cls.__name__)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    file_path = os.path.join(folder_path, name)
    # 判断如果文件存在的话去查对应文件的信息返回
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)


def check_all_obj(cls):
    # 拼接路径，判断文件夹路径是否存在，如果不存在创建该路径的文件夹
    folder_path = os.path.join(settings.DB_PATH, cls.__name__)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    return os.listdir(folder_path)
