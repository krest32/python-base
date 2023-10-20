import numpy as np

a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print('我们的数组是：')
print(a)

print('调用 argmax() 函数：')
print(np.argmax(a))

print('展开数组：')
print(a.flatten())

print('沿轴 0 的最大值索引：')
maxindex = np.argmax(a, axis=0)
print(maxindex)

print('沿轴 1 的最大值索引：')
maxindex = np.argmax(a, axis=1)
print(maxindex)

print('调用 argmin() 函数：')
minindex = np.argmin(a)
print(minindex)

print('展开数组中的最小值：')
print(a.flatten()[minindex])

print('沿轴 0 的最小值索引：')
minindex = np.argmin(a, axis=0)
print(minindex)

print('沿轴 1 的最小值索引：')
minindex = np.argmin(a, axis=1)
print(minindex)