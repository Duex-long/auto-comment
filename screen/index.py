from logger.index  import check_dir,create_dir,get_cwd


#  bowers 实现 webdriver()接口
class Screen_logger(bowers):
    dir_name='screen'
    def __init__(self):
        path = get_cwd() + self.dir_name
        has_dir = check_dir(path)
        if not has_dir:
            create_dir(path)

