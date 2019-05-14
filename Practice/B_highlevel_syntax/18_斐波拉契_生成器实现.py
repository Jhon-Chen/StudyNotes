def fibonacci(n):
    # 定义数列的前两个值
    a = 0
    b = 1

    # 定义当前位置下标
    current_index = 0
    while True:
        # 定义要返回的值
        result = a
        # 生产新的a, b值
        a, b = b, a + b
        # 下标增加
        current_index += 1
        yield result


# 创建生成器
fib = fibonacci(20)
value = next(fib)
print(value)
for i in range(20): 
    print(next(fib))


