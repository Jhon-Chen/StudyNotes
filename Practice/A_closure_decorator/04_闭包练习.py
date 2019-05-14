# 定义外层函数
def make_avg():
    data = list()
    # 定义内层函数
    def addnumber(value):
        data.append(value)
        total = sum(data)
        return total / len(data)
    return addnumber

# 调用函数
result = make_avg()
print(result(100))
print(result(200))
