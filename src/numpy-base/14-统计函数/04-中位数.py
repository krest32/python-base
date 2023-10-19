import numpy as np

a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
print('我们的数组是：')
print(a)

print('调用 median() 函数：')
print(np.median(a))

print('沿轴 0 调用 median() 函数：')
print(np.median(a, axis=0))

print('沿轴 1 调用 median() 函数：')
print(np.median(a, axis=1))