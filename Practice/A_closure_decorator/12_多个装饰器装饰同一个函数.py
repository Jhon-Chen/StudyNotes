# 模拟实现文字加粗的装饰器
def makeBlod(func):
    # 定义内层函数 实现文字加粗
    def wrapped():
        return "<b>" + func() +"</b>"
    return wrapped 

# 模拟实现文字倾斜装饰器
def makeItalic(func):
    # 定义内层函数实现文字倾斜
    def wrapped():
        return "<I>" + func() + "</I>"
    return wrapped

# 使用makeBlob装饰器修饰
@makeBlod 
def test1():
    return "i need a hug form gakki"

# 使用makeItalic装饰器
@makeItalic 
def test2():
    return "i need a hug from gakki"

# 使用多个装饰器
@makeBlod
@makeItalic
def test3():
    return "i need a hug from gakki"

# 观察结果
print(test1())
print(test2())
print(test3())
