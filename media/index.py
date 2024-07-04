from abc import ABCMeta,abstractmethod

class Media(metaclass=ABCMeta):

    # 依赖bower运作
    def __init__(self,bower):
        self._bower = bower
   
    # 启动
    @abstractmethod
    def open(self):
        pass
    # 检查登陆
    @abstractmethod
    def check_login(self):
        pass
    # 登陆
    @abstractmethod
    def login(self):
        pass
    # 前往目标地址 并且评论
    @abstractmethod
    def lock_target(self):
        pass
