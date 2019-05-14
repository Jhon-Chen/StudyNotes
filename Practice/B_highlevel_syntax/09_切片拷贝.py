# 导入模块
import copy
# 定义元组
a = [1, 2]
b = [3, 4]
c = (a, b)
# 拷贝c使用切片拷贝实现
d = c[:]

# 拷贝后c, d的内容
print('c= %x, d= %x' % (id(c), id(d)))
print('d[0]= %x, c[0]= %x, a= %x' % (id(d[0]), id(c[0]), id(a)))
