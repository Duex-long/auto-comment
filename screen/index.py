from logger.index  import check_dir,create_dir,get_cwd,get_time_format


# selenium截图模块，需要注入依赖项
class Screen_logger():
    dir_name='/screen_dir/'
    _bower=None
    def __init__(self,bower):
        path = get_cwd() 
        has_dir = check_dir(path + self.dir_name)
        print(has_dir,'has_dir',path + self.dir_name)
        if not has_dir:
            create_dir(path, self.dir_name)
        #注入依赖 
        self._bower = bower
    
    # 拍照
    def screenshot(self): 
        try:
            path =get_cwd() +  self.dir_name + get_time_format() + '.png'
            self._brower.save_screenshot(path)
            return path
        except error:
            return 'failed'
        



