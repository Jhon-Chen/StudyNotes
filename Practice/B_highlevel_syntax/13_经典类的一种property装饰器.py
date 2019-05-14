# 定义
class Goods:
    @property
    def price(self):
        return "Gakki~"

# 调用
obj = Goods()
result = obj.price # 自动执行@property修饰的price方法 并获取方法的返回值
print(result)


