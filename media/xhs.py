from .index import Media


class XHSMedia(Media):
    _url = 'https://www.xiaohongshu.com/notification'
    def __init__(self,bower):
        super().__init__(bower)
        self._name = 'xhs'
    def open(self,url):
        self._bower.get(url) 
        self.browers.implicitly_wait(10)
    def open_index(self):
        print('启动')
        self._bower.get(self._url)    
        self.browers.implicitly_wait(10)
    def check_login(self):
        return True
    def login(self):
        return True
    def lock_target(self):
        return True
    def append_comment(self):
        return True