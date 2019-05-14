def func1(*args, **kwargs):
    # 输出参数
    print(args)
    print(kwargs)

def func2(*args, **kwargs):
    # args = (10, 20, 30) kwargs = {'age':18, 'name':xxx}
    # ！！!注意下面的写法
    # func1(args, kwargs)   ---这是未拆包的写法
    # func1(*args, **kwargs)   ---这是拆包的写法
    # 拆包前
    # func1(args, kwargs)
    # func1((10, 20, 30) kwargs = {'age':18, 'name':xxx})
    # 拆包后
    # func1(*args, **kwargs)
    # func1(10, 20, 30, age=18, name='xxx')
    func1(*args, **kwargs)

# 调用func2()
func2(10, 20, 30, age=18, name='xxx')

