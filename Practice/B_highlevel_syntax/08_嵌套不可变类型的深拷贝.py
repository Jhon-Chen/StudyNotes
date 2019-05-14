# 导入模块
import copy

# 定义元组
a = [1, 2]
b = [3, 4]
c = (a, b)
# 对元组进行浅拷贝
d = copy.deepcopy(c)
# 拷贝后c, d的内容
print('c =', c, 'd =', d)
print('c = %x, d = %x' % (id(c), id(d)))
print('d[0] = %x, c[0] = %x, a = %x' % (id(d[0]), id(c[0]), id(a)))
