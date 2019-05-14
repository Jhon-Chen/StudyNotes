class Fibonacci():
    def __init__(self, num):
        # 通过构造方法 保存num到类的成员属性中
        self.num = num
        # 定义变量保存斐波拉契数列前两个数的值
        self.a = 0
        self.b = 1
        # 记录当前的变量下标
        self.current_index = 0

    def __iter__(self):
        # 返回迭代器 因为它本身就是一个迭代器
        return self

    def __next__(self):
        # 判断是否生产完毕
        if self.current_index < self.num:
            # 返回
            result = self.a
            # 交换两个变量的值
            self.a, self.b = self.b, self.a + self.b
            self.current_index += 1
            return result
        else:
            # 停止迭代
            raise StopIteration


if __name__ == '__main__':
    # 创建迭代器
    fib = Fibonacci(20)
    # 使用迭代器 输出斐波拉契数列
    for value in fib:
        print(value, end=" ")
