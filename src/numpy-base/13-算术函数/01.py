import numpy as np

a = np.arange(9, dtype=np.float_).reshape(3, 3)
print('第一个数组：')
print(a)

print('第二个数组：')
b = np.array([10, 10, 10])
print(b)

print('两个数组相加：')
print(np.add(a, b))

print('两个数组相减：')
print(np.subtract(a, b))

print('两个数组相乘：')
print(np.multiply(a, b))

print('两个数组相除：')
print(np.divide(a, b))
