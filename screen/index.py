from logger.index  import check_dir,create_dir,get_cwd,get_time_format


# selenium截图模块，需要注入依赖项
class Screen_logger():
    dir_name='/screen_dir'
    _bower=None
    def __init__(self,bower):
        path = get_cwd() 
        has_dir = check_dir(path + self.dir_name)
        if not has_dir:
            create_dir(path, self.dir_name)
        #注入依赖 
        self._bower = bower
    
    # 拍照
    def screenshot(self): 
        try:
            path = get_cwd() +  self.dir_name + '/'+ get_time_format()+  '.png'
            print(self._bower,'是否有brower')
            print(self._bower.save_screenshot(path))
            return path
        except Exception as e:
            path = get_cwd() +  self.dir_name + '/'+ get_time_format()+  '.png'
            print('截图失败',e)
            return 'failed'
        



