from .index import Media
from time import sleep
from dmail.index import Mail_Helper
from selenium.webdriver.common.keys import Keys

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
        mock_target = 'https://www.xiaohongshu.com/explore/6686092f000000001e01208b?xsec_token=AB44q93b1xNfMmzoNsVpW4qiH0u9Ko2OXTAvDm1nVZYXQ=&xsec_source=pc_feed'
        mock_target2 = 'https://www.xiaohongshu.com/explore/668403cb000000001c025beb?xsec_token=AB93M1t-LWOC6wEKnTMcuCEPp06fJUqyioxw6RsaMkzSE=&xsec_source=pc_feed'
        # self.lock_target(mock_target,"谁掏钱就买谁喜欢的呗。") 
        self.lock_target(mock_target2,"你卖了就开始拉升了，你不卖永远拉不了") 
        
        
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
    def lock_target(self,url,comment):
        self.open(url)
        # spa 需要等待页面load
        sleep(3)
        try:

            # inner 
            # parentContainer
            parent_container = self._bower.getElementByClass('content-edit')
            target_container = self._bower.getElementByClass('inner',parent_container)
            # 点击触发输入框
            target_container.click()
            insert_element = self._bower.getElementById('content-textarea')
             # 输入框 是个p
            # 模拟输入文本
            insert_element.send_keys(comment)  # 输入文本
            insert_element.send_keys(Keys.RETURN)
            sleep(3)
            comment_screen = self._bower.screenshot()
            print('截图',comment_screen)
            return comment_screen
        except Exception as e:
            print('评论出错',e)
            return False
 