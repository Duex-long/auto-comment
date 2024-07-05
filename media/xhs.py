from .index import Media
from time import sleep
from dmail.index import Mail_Helper
from logger.index import Logger,get_cwd,get_time_format
from selenium.webdriver.common.keys import Keys
import urllib.parse
import random
import re
# 记录地址
log_path = get_cwd() + '/record/'
record = Logger(log_path)
# 邮件接收者
receiver = '852040420@qq.com'
# 页面加载等待
PAGE_INIT_WAIT = 10
# SPA等待
PAGE_SPA_WAIT = 3
#基本操作等待
PAGE_EVENT_WAIT = 1
# 等待时间
polling_seconds = 10
# 暂停最小随机
disguise_min = 1
# 暂停最大随机
disguise_max = 6

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



list_str = """https://www.xiaohongshu.com/explore/65aa4212000000002d0349a8?xsec_token=ABj9KxZCAoI30TTSg8e6-EyskLH-IKv6D4A32qGOtjKIk=&xsec_source=pc_search,
https://www.xiaohongshu.com/explore/65d8012e0000000001028ff3?xsec_token=ABacagSBDeM8tG4ZhJ56JxchCgmg3mwQRvkOycbDxrDZk=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/65d6bce80000000001029245?xsec_token=AB2ms6ayC5ui1YwHtsisCWlbeSRj3GGWWzKvU5AzkKqIQ=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/65e0a59d000000000102a512?xsec_token=AB4VfFWk6xgkc8Wjony9-rBbNtgCE_IL8BY4L-GmRCAhs=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/65b1e3970000000011013155?xsec_token=ABCqUytRmvpDH8ksJMNqGL7kxBcIWPKa-CgqEaJWOQHZA=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/666a57db000000000e03115a?xsec_token=ABcWNPDWUtvBlwVjW-cf2627CF4jBm-YhNGBFVXgzw-iM=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/664d6d3b000000000f00fe78?xsec_token=AB-evsZ8xhY8_-JJeFND3ZQjdue9z25w-TKsK77Ha5C4Y=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/664d3bf400000000050073d7?xsec_token=AB-evsZ8xhY8_-JJeFND3ZQtNni2Uz7yhp9R80yzHBR60=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/665469760000000014018d41?xsec_token=AB0EgRywuNuiJUjbTVf69-ap4vp40dZbXXe5JTfc8tV4k=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/667a2b0a000000001d01a608?xsec_token=ABthygRa-baj-mEu--HRjAGzZ3MOmnk6M_N2QYbqn24Uk=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/65e8b7f4000000000600e131?xsec_token=ABP3cTX-NAV0hXgzpXhnB9eDgV7tqySnhTbx4qQh-UfvU=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/66553af6000000001500b23d?xsec_token=ABbdgrWnqY-mQ7VhF1OuL4BOJynxPC9NJeiSwivIsA5ck=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/664db16c000000001303e88e?xsec_token=AB-evsZ8xhY8_-JJeFND3ZQn2eggbMKjlOAlfcFA0V5Lk=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/6646b2ea000000001e02640d?xsec_token=ABalEeKp3AOmd3lovEI2VOHZG-qNsAX9o5j4VuBQHgtXs=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/6634539c000000001e02295d?xsec_token=ABYmaOMaMck-55N1CynWjhwmoM5bsDOA6r73SODz1zfSQ=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/665469720000000014018cf2?xsec_token=AB0EgRywuNuiJUjbTVf69-alqfrfYgeLXHaKQq6b2dzQQ=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/65e5839c000000000102a1d8?xsec_token=ABCrIPJyH8CUhURixyiwftaVuroqx_tNFcso2ObNLjYN4=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/664c7d9e00000000160113a9?xsec_token=ABL-osveQT7UkK8t9bm0G9acsXuIgTvlQjXdvaaKzKfQI=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/66220ef0000000000103344a?xsec_token=ABuoMK2jO0Ri9q-I2twypZ-pCz2V1dWI2xrsBUh3ni-tw=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/664338d9000000001e0340d5?xsec_token=ABbbL21shtezJwK1xpSFBo7-KkcvvktCsE8jcpAGLgFVo=&xsec_source=pc_search,

https://www.xiaohongshu.com/explore/6683943d000000001c025672?xsec_token=AB0dyBHV1NnRhcrXk3JgawKX4w_P6iKV7-pxjlQigy8n0=&xsec_source=pc_search"""


target_list  = list_str.split(',')

comment_list = ['哪个牌子呀，我家现在吃的是lifelinecare我对比下要不要换','我家吃的lifelinecare不错，已经四岁了一直买他们家鱼油','当时比较在意DHA含量，所以买了高含量的lifelinecare']

print(target_list,'target_list')
mail = Mail_Helper()
class XHSMedia(Media):
    _login_mark = 0
    _url = 'https://www.xiaohongshu.com/notification'
    _search_origin_url = 'https://www.xiaohongshu.com/search_result'
    def __init__(self,bower):
        super().__init__(bower)
        self._name = 'xhs'
    def open(self,url):
        self._bower.browers.get(url) 
        self._bower.browers.implicitly_wait(PAGE_INIT_WAIT)
    def open_index(self):
        print('启动')
        self._bower.browers.get(self._url)    
        self._bower.browers.implicitly_wait(PAGE_INIT_WAIT)
        # 等待小红书未登录弹窗
        sleep(PAGE_SPA_WAIT)
        # 检查登陆
        self.check_login()  
        # 模拟用户

        for target_url_item in target_list:
            self.lock_target(target_url_item,comment_list[random.randint(0,2)])
        # self.disguise()
        return True
    
    def check_login(self,send=True):
        # 检查login容器
        try:
            login_container = self._bower.getElementByClass('login-container')
            if login_container:
                # 未登录的情况下进行屏幕快照
                print(login_container,'登录容器')
                if send:
                    try:
                        login_screen = self._bower.screenshot()
                        print(login_screen,'截图')
                        mail.file_builder(login_screen,'查看内容.png')
                        mail.header_builder('852040420@qq.com','需要扫马儿')
                        mail.message_builder('附件中有内容')
                        mail.send_mail(receiver)
                        
                    except Exception as mail_error:
                        print('邮件发送错误',mail_error)
                # 轮询
                self._login_mark +=1
                need_send = bool(self._login_mark % 4 == 0)
                sleep(polling_seconds)
                print(need_send,'需要发送邮件吗')
                self.check_login(need_send)
        except Exception as e:
            print(e,'错误信息')
            print('登陆成功')
            return True
        
    def login(self):
        return True
    def lock_target(self,url,comment):
        self.open(url)
        record_data = {}
        # spa 需要等待页面load
        sleep(PAGE_SPA_WAIT)
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
            # 因enter按键同样被绑定发送事件，模拟键盘 小红书的insert目前没有发现埋点，直接贴内容即可
            insert_element.send_keys(Keys.RETURN)
            # 等待3s接口/页面响应
            sleep(PAGE_SPA_WAIT)
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
        self._bower.window_scroll_by_Y(random.randint(300,800))
        return comment_result
    def disguise(self):
        # 回首页
        # self.open(self._url)
        home_button = self._bower.getElementById('link-guide')
        if home_button :
            home_button.click()
        else:
            self.open(self._url)
        sleep(PAGE_EVENT_WAIT)
        # 获取模拟次数
        scroll_num = random.randint(disguise_min,disguise_max)
        # 根据 scroll_num 次数 模拟操作 滚动 点击 红心
        for i in range(scroll_num):
            self._bower.window_scroll_by_Y(random.randint(300,800))
            # 每次做完操作稳定一下
            sleep(PAGE_SPA_WAIT)
        
        sleep(PAGE_SPA_WAIT)

    def keyword_search(self,keyword):
        encode_keyword = XHSMedia._search_decode(keyword)
        search_url = f'{self._search_origin_url}?keyword={encode_keyword}&source=unknown'
        self.open(search_url)
    # 编码
    @staticmethod
    def _search_encode(decode_str):
        encoded_str = urllib.parse.quote(urllib.parse.quote(decode_str))
        return  encoded_str
    # 解码
    @staticmethod
    def _search_decode(encoded_str):
        decoded_str = urllib.parse.unquote(urllib.parse.unquote(encoded_str))
        return decoded_str

 