import numpy as np

a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')
# 默认按行

print('展开的数组：')
print(a.flatten())
print('\n')

print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))
