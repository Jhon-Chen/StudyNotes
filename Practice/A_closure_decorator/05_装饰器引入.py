# 第一波
def foo():
    print("foo")

foo()

# 第二波
def fool():
    print("fool")

fool = lambda x: x + 1
# 这一句只会执行lambda表达式，而不再是原来的fool函数了，因为fool已经被重新指向了一个匿名的函数
print(fool(5))

