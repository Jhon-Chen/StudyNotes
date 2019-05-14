# 定义外部函数
def line_conf(a, b):
    # 定义内层函数
    def line(x):
        print('a = ', a) # 注意 此行代码现在运行就会输出 a = 1
        # 使用了外部函数中的 a, b 两个变量
        return x*a + b
    return line
