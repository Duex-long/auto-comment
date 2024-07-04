from .index import Media
from time import sleep
from dmail.index import Mail_Helper

receiver = '852040420@qq.com'
polling_seconds = 10

mail = Mail_Helper()
class XHSMedia(Media):
    _url = 'https://www.xiaohongshu.com/notification'
    def __init__(self,bower):
        super().__init__(bower)
        self._name = 'xhs'
    def open(self,url):
        self._bower.browers.get(url) 
        self._bower.browers.implicitly_wait(10)
    def open_index(self):
        print('启动')
        self._bower.browers.get(self._url)    
        self._bower.browers.implicitly_wait(10)
        # 等待小红书未登录弹窗
        sleep(4)
        # 检查登陆
        self.check_login() 

        # 锁定目标
        mock_target = 'https://www.xiaohongshu.com/explore/63fa0f720000000013033b48?xsec_token=ABuVs-3eDbtBfMHKwjHNr_heTCCV6PnlUH9uikanTKO8c=&xsec_source=pc_feed'
        self.lock_target(mock_target) 

    def check_login(self):
        # 检查login容器
        try:
            login_container = self._bower.getElementByClass('login-container')
            if login_container:
                # 未登录的情况下进行屏幕快照
                print(login_container,'登录容器')
                login_screen = self._bower.screenshot()
                print(login_screen,'截图')
                # mail.file_builder(login_screen,'查看内容.png')
                # mail.header_builder('852040420@qq.com','需要扫马儿')
                # mail.message_builder('附件中有内容')
                # mail.send_mail(receiver)
                sleep(polling_seconds)
                # 轮询
                self.check_login()
        except:
            print('登陆成功')
            return True
        
    
    def login(self):
        return True
    def lock_target(self,url):
        self.open(url)
        try:
            # inner 
            target_container = self._bower.getElementByClass('inner')
            # 点击触发输入框
            target_container.click()
            # 输入框 是个p
            insert_element = self._bower.getElementById('content-textarea')
            # 模拟输入文本
            insert_element.send_keys("nice picture")  # 输入文本
        except:
            return False
        return True
    def append_comment(self):
        return True