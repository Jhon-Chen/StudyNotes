# 定义外层函数
def line_conf(a, b):
    # 定义内层函数
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))
