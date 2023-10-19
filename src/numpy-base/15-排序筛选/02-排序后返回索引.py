import numpy as np

# numpy.argsort() 函数返回的是数组值从小到大的索引值。
x = np.array([3, 1, 2])
print('我们的数组是：')
print(x)

print('对 x 调用 argsort() 函数：')
y = np.argsort(x)
print(y)

print('以排序后的顺序重构原数组：')
print(x[y])

print('使用循环重构原数组：')
for i in y:
    print(x[i], end=" ")