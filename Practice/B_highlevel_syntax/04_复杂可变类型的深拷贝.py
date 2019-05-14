# 导入模块
import copy

# 列表的地址（可变类型）
A = [1, 2]
B = [3, 4]
C = [A, B]
print('A的地址：%x' % id(A))
print('B的地址：%x' % id(B))
print('C[0]的地址：%x' % id(C[0]))
print('C[1]的地址：%x' % id(C[1]))

print('-' * 40)
D = copy.deepcopy(C)
print('A的地址：%x' % id(A))
print('C[0]的地址：%x' % id(C[0]))
print('D[0]的地址：%x' % id(D[0]))

