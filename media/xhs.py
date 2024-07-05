from .index import Media
from time import sleep
from dmail.index import Mail_Helper
from logger.index import Logger,get_cwd,get_time_format
from selenium.webdriver.common.keys import Keys
import random
import re
# 记录地址
log_path = get_cwd() + '/record/'
record = Logger(log_path)
# 邮件接收者
receiver = '852040420@qq.com'
# 等待时间
polling_seconds = 10
# 暂停最小随机
disguise_min = 10
# 暂停最大随机
disguise_max = 50



#example
    # 方法1
    # 锁定目标
    # mock_target = 'https://www.xiaohongshu.com/explore/6686092f000000001e01208b?xsec_token=AB44q93b1xNfMmzoNsVpW4qiH0u9Ko2OXTAvDm1nVZYXQ=&xsec_source=pc_feed'
    # mock_target2 = 'https://www.xiaohongshu.com/explore/668403cb000000001c025beb?xsec_token=AB93M1t-LWOC6wEKnTMcuCEPp06fJUqyioxw6RsaMkzSE=&xsec_source=pc_feed'
    # self.lock_target(mock_target,"谁掏钱就买谁喜欢的呗。") 
    # target_insert_content = '插入内容'
    # file_path = self.lock_target(mock_target2,target_insert_content) 
    # 方法2
    # 发送数据
    # for target_url in target_list:
    #     mock_message = send_list[random.randint(0, 4)]
    #     self.lock_target(target_url,mock_message)



print(target_list,'target_list')
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
        # self.check_login() 
        # 模拟用户
        self.disguise()
        
        return True
   
    def check_login(self):
        # 检查login容器
        try:
            login_container = self._bower.getElementByClass('login-container')
            if login_container:
                # 未登录的情况下进行屏幕快照
                print(login_container,'登录容器')
                login_screen = self._bower.screenshot()
                print(login_screen,'截图')
                mail.file_builder(login_screen,'查看内容.png')
                mail.header_builder('852040420@qq.com','需要扫马儿')
                mail.message_builder('附件中有内容')
                mail.send_mail(receiver)
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
        record_data = {}
        # spa 需要等待页面load
        sleep(3)
        comment_result = None
        try:
            # 获取输入框元素的container（会有重名样式 所以必须逐步缩小范围）
            parent_container = self._bower.getElementByClass('content-edit')
            # 在改样式下的inner才是激活输入框的Element
            target_container = self._bower.getElementByClass('inner',parent_container)
            # 这个div被注入了click事件控制content-textarea展示隐藏
            target_container.click()
            # 之后输入文本被激活展示（这种操作看似多余，实则是模拟操作，会有埋点记录）
            insert_element = self._bower.getElementById('content-textarea')
            # 模拟输入文本
            insert_element.send_keys(comment)  # 输入文本
            # 因enter按键同样被绑定发送事件，模拟键盘
            insert_element.send_keys(Keys.RETURN)
            # 等待3s接口/页面响应
            sleep(3)
            # 截图
            comment_screen = self._bower.screenshot()
            # 记录数据
            record_data["file_path"] = comment_screen
            # 保存返回值
            comment_result = comment_screen
        except Exception as e:
            print('评论出错',e)
            record_data["file_path"]  = '失败'
             # 保存返回值
            comment_result =  False

        record_data["target"] = url
        record_data["comment"] = comment
        record_data["time_stamp"] = get_time_format()
        try:
            record.append_data(record_data)
        except Exception as record_err:
            print('record失败')
        return comment_result
    def disguise(self):
        # 回首页
        # self.open(self._url)
        home_button = self._bower.getElementById('link-guide')
        if home_button :
            home_button.click()
        else:
            self.open(self._url)
        sleep(2)
        scroll_num = random.randint(disguise_min,disguise_max)
        self._bower.window_scroll_by_Y(300)

        

 