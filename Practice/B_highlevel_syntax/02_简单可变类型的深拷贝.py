# 导入模块
import copy

# 列表的地址（可变类型）
list1 = [1, 2]
print('list1的内存地址：%x' % id(list1))

# 针对可变类型，进行的深拷贝会创建新的空间
list2 = copy.deepcopy(list1)
print('list2的内存地址：%x' % id(list2))

# 改变list2，添加新的元素，观察其内存地址的变化
list2.append(520)
print('list2新的内存地址：%x' % id(list2))

# 打印结果
print(list2)
print(list1)
