import numpy as np

a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
print('我们的数组是：')
print(a)

print('调用 nonzero() 函数：')
print(np.nonzero(a))