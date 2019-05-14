# 导入模块
import copy

# 定义元组
a = (1, 2, 3)

# 对元组进行浅拷贝
a1 = copy.deepcopy(a)

# 查看a, a1的内容
print(a, a1)

# 查看a, a1的地址
print('a: %x, a1: %x' % (id(a), id(a1)))
