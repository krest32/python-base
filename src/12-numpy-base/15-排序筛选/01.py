import numpy as np

a = np.array([[3, 7], [9, 1]])
print('我们的数组是：')
print(a)

print('调用 sort() 函数：')
print(np.sort(a))

print('按列排序：')
print(np.sort(a, axis=0))

# 在 sort 函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print('我们的数组是：')
print(a)

print('按 name 排序：')
print(np.sort(a, order='name'))