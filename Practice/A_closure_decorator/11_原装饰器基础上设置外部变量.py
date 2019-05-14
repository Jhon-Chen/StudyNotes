# 定义函数 准备使用多层装饰器
def test_arg(s="hello"):
    # 闭包函数function_out为外层函数
    def function_out(func):
        # function_in为内层函数
        def function_in(a):
            print("正在进行验证---, a = ", a, s)
            # func ---> login
            return func(a)
        return function_in
    return function_out 

# 装饰过程：
# 调用test_arg("loginxx")
# 将上一步得到的返回值，即function_out返回，然后function_out(login)
# 将function_out(login)的结果返回，即function_in
# 让login = function_in,即login现在指向function_in
@test_arg("loginxx")
def login(a):
    print("---开始登陆---, a = ", a)
    return a

# 装饰过程
# 调用test_arg("register")
# 将上一步得到的返回值，即function_out返回，然后function_out(register)
# 将function_out(register)的结果返回，即function_in
# 让register = function_in,即register现在指向function_in
@test_arg("register")
def register(a):
    print("---开始注册---, a = ", a)

# 调用login函数，实质上调用function_in ---> login
result = login(10)
print("result = ", result)

# 调用register，实质上先调用function_in ---> register
register(100)

