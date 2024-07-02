from selenium import webdriver
from time import sleep
from logger.index import log_to_json,get_time_format,get_cwd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
    screen_path ='/screen/'
    # browers 驱动实例
    browers=None
    #启动状态
    init_state=False
    # 登录状态
    login_state=False
    # 工作状态
    working_state=False

    def __init__(self):
        self._init()
    @log_to_json
    def _init(self):
        chrome_options = init_config()
        browers = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options,service=Service(ChromeDriverManager().install()))
        # 设置webdriver 放置检测
        self._wipe_driver()
        browers.get('https://www.xiaohongshu.com/notification')
        self.browers = browers
        self.init_state = True
    
    # 抹除webdriver信息
    def _wipe_driver(self,browers):
            browers.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
            "source":""" Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"""
        })
    # 截屏
    def screenshot(self):
        path =get_cwd() +  self.screen_path + get_time_format() + '.png'
        self.browers.save_screenshot(path)
        print(f"窗口快照已保存到 {path}")

if __name__ == '__main__':
    driver = auto_comment()
    driver.screenshot()