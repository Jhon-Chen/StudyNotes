def fibonacci(n):
    a = 0
    b = 1
    current_index = 0
    while current_index < n:
        # 定义要返回的值
        result = a
        a, b = b, a + b
        current_index += 1

        # 这一句的赋值必须写 否则send()的结果无法输出
        parms = yield result
        print("send-----", parms)


fib = fibonacci(20)
value = fib.send(None)
print(value)

value = fib.send(666)
print(value)

value = fib.send(999)
print(value)

print(next(fib))
print(next(fib))

# send进去的值 并不会被返回 
# 只有在传入时 赋值给这个parms 才能看出send确实传值进了函数
