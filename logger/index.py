import os
import json
from functools import wraps
from datetime import datetime

def get_cwd():
    return os.getcwd()

def get_time_format():
    return datetime.now().isoformat()

def log_to_json(func):
    # 装饰函数
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        log_data = {
            'function': func.__name__,
            'args': args[1:],  # 跳过 'self'
            'kwargs': kwargs,
            'timestamp':get_time_format(),
            'result':result
        }
        logger.append_data(log_data)

        return result
    return wrapper
def check_dir(path):
    if (not os.path.exists(path=path)):
        return False
    else:
        return True

def create_dir(path,name):
    is_create_dir = check_dir(path=path+name)
    if(is_create_dir):
        return True
    else :
        os.mkdir(path+name)
        return True


log_path = get_cwd() + '/logger/'
# 括号是继承
class Logger():
    # 目录
    path=''
    # 路径
    full_path_name=''
    def __init__(self,path,name=''):
        self.path = path
        self._check_file(name)

    def _hash_file_name(self,name):
        return self.path + name +'logger.json'

    def _check_file(self,name=''):
        full_path_name = self._hash_file_name(name)
        self.full_path_name = full_path_name
        if not os.path.exists(full_path_name ):
                with open(full_path_name, 'w') as f:
                    json.dump([], f)

    # 添加数据
    def append_data(self,log_data):
        print(self.full_path_name,'self.path',log_data)
        with open(self.full_path_name, 'r+') as f:
                data = json.load(f)
                # 4. 追加新日志数据
                data.append(log_data)
                f.seek(0)
                json.dump(data, f, indent=4)
    # 添加快照


logger = Logger(log_path)