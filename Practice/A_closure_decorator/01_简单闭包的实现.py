# 定义外层函数 function_out
def function_out(num):
    print ('-----function out-----,num = ', num)
    # 定义内层函数
    # 在函数内部再定义一个函数，并且这个函数用到了外层函数的变量，那么把这个函数以及用到的相关的变量称之为内嵌函数
    def function_in(num_in):
        print('-----function in-----,num = ', num)
        print('-----function in-----,num_in = ', num_in)

    return function_in

# 调用function_out() 把100传给num
# result 保存的是 function_in() 的地址
result = function_out(100)

# 调用内层函数function_in()
result(88)

