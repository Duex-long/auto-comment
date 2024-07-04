


class Console:
    def error(self,message):
        print(f"\033[31m{message}\033[0m")
    def warning(self,message):
        print(f"\033[33m{message}\033[0m")
    def log(self,message):
        print(f"\033[32m{message}\033[0m")
    def light(self,message):
        print(f"\033[34m{message}\033[0m")