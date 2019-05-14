# 导入模块
import copy
# 定义字典
dict = {'age':[1, 2]}

# 字典拷贝，是通过对象自带的copy()方法实现的
dict2 = dict.copy()

# 查看字典的值
print(dict, dict2)

# 查看字典地址
print('dict= %x, dict2= %x' % (id(dict), id(dict2)))

# 修改dict字典的值
dict['age'][1] = 100
dict['age'].append(50)

# 查看字典的值
print(dict, dict2)
