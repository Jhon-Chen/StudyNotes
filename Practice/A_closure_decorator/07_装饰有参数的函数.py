# 闭包函数function_out为外层函数
def function_out(func):
    # function_in为内层函数
    def function_in(a):
        print("正在进行验证---, a = ", a)
        # func ---> login
        func(a)
    return function_in


# 使用装饰器
@function_out
# 定义login函数
def login(a):
    print("开始登陆---, a = ", a)
# 调用了Login函数,实际上是调用了function_in函数
login(10)
