# 闭包函数function_out为外层函数
def function_out(func):
    # function_in为内层函数
    def function_in(*args, **kwargs):
        print("正在进行验证---")
        print("function_in参数：", args, kwargs)
        # func ---> login
        func(*args, **kwargs)
    return function_in


# 使用装饰器
@function_out
# 定义login函数
# *args,**kwargs 是不定长可变参数
def login(*args, **kwargs):
    print("开始登陆---")
    print("login参数：", args, kwargs)
# 调用了Login函数,实际上是调用了function_in函数
login(10,20,a=100,b=900)
