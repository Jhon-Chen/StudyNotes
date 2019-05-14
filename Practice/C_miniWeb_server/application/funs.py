import time
from application import urls

# 装饰器路由
def route(path):
    # 外层函数
    def func_out(func):
        # 添加路径到字典中
        urls.route_dict[path] = func
        # 内层函数
        def func_in():
            return func()
        return func_in
    return func_out

# 首页
@route("/index.py")
def index():
    return "This is index show!"

# 内容页
@route("/center.py")
def center():
    return "This is center show!"

# 动态显示网页时间
@route("/gettime.py")
def gettime():
    return "The time is %s" % time.ctime()

