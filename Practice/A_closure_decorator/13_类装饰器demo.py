class Test(object):
    def __init__(self, func):
        print('---初始化---')
        print('func name is %s'% func.__name__)
        self.__func = func 
    # 重写__call__方法
    def __call__(self):
        print('---装饰器中的功能---')
        self.__func()

# 说明
# 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
# 并且会把test这个函数名当做参数传递带__inti__方法中
# 即在__init__方法中的属性__func指向了test指向的函数
# test指向了用Test创建出来的实例对象
# 当在使用test()进行调节时，就相当于让这个对象()，因此会调用这个对象的__call__方法
# 为了能够在__call__方法中调用原来test只想的函数体，所以在__init__方法中就需要一个实例属性来保存
# 所以才有了self.__func = func这一句代码，从而在调用__call__方法中能够调用到test之前的函数体


@Test
def test():
    print('---test---')

test()
