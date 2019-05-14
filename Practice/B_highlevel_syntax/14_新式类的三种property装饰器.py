# 定义
class Goods:
    """python3中默认继承object类
    以python2,3执行此程序结果不同 因为只有在python3中才有@xxx.setter和@xxx.deleter"""
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')

# 调用
obj = Goods()
obj.price  # 自动执行@property修饰的price方法 并获取返回的值
obj.price = 123  # 自动执行 @price.setter修饰的price方法 并将123赋值给方法的参数
del obj.price  # 自动执行@price.deleter修饰的price方法

