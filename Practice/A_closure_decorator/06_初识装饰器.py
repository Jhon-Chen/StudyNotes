# 闭包函数function_out为外层函数
def function_out(func):
    # function_in为内层函数
    print("这是内层函数")
    def function_in():
        print("正在验证-----")
        func()
    return function_in


# 使用装饰器
@function_out
# 定义login函数
def login():
    print("---开始登陆---")

# 调用login函数，实际上也调用了function_in函数
login()
