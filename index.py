from selenium import webdriver
from time import sleep
from screen.index import Screen_logger
from logger.index import log_to_json,get_time_format,get_cwd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from media.xhs import XHSMedia
from console.index import Console
import os

console = Console()

def init_config():
    # 初始化配置
    chrome_options = webdriver.ChromeOptions()
    # 启用全屏模式
    # options.add_argument("--start-fulls creen")
    # 持久化运行
    chrome_options.add_experimental_option('detach', True)
    # 无窗口模式
    # chrome_options.add_argument('--headless')
    return chrome_options

class auto_comment:
    url:'https://www.xiaohongshu.com/notification'
    #截图保存目录
    # media 工厂
    mediaFactory=None
    #media
    media=None
    # browers 驱动实例
    browers=None
    #启动状态
    init_state=False
    # 登录状态
    login_state=False
    # 工作状态
    working_state=False
    # 屏幕功能注入
    screen_carema=None

    def __init__(self,mediaFactory):
        self.mediaFactory = mediaFactory
        self._init()
        
    @log_to_json
    def _init(self):
        # 创建webdriver配置
        chrome_options = init_config()
        # 初始化浏览器
        browers = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options,service=Service(ChromeDriverManager().install()))
        self.browers = browers
        # 设置webdriver 放置检测
        self._wipe_driver()
         # 加载截图功能
        self.screen_carema = Screen_logger(browers)
        # 预检
        self.init_state = self._pre_check()
        # 加载社交平台
        self._load_media()
        # 打开平台
        self.media.open_index()
    # 抹除webdriver信息
    def _wipe_driver(self):
        # 修改属性
        # self._inject_js_code(""" Object.defineProperty(navigator,'webdriver',{get:()=>undefined})""")
        # 注入js
        js_path ='./stealth.min.js'
       
        if(os.path.exists(js_path)):
            with open(js_path) as f_js:
                js = f_js.read()
                self._inject_js_code(js)

    def _pre_check(self):
         # 预检
        self.browers.get('https://bot.sannysoft.com/')
        self.browers.implicitly_wait(10)
        element = self.browers.find_element_by_id('webdriver-result')
        state_text = element.text
        if('missing' in state_text):
            console.log('预检通过')
            return True
        else:
            console.error('预检失败')
            return False

    # 加载js
    def _inject_js_code(self,code):
        self.browers.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                    "source": code
        })
    def _load_media(self):
        self.media =self.mediaFactory(self.browers)
    
    # 截屏
    def screenshot(self):
        file_path = self.screen_carema.screenshot()

if __name__ == '__main__':
    driver = auto_comment(XHSMedia)

    # 测试初始化
    # screen = Screen_logger()