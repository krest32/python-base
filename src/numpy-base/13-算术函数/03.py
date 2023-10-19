import numpy as np

a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print('第一个数组：')
print(a)

print('第二个数组：')
print(b)

print('调用 mod() 函数：')
print(np.mod(a, b))

print('调用 remainder() 函数：')
print(np.remainder(a, b))
