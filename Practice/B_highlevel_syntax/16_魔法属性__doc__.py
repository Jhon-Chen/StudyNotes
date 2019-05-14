class Foo:
    """描述类信息 这一条注释将会被输出"""
    def start(self):
        """这一条也可以被输出"""
        pass

f = Foo()
print(Foo.__doc__)
print(Foo.start.__doc__)

