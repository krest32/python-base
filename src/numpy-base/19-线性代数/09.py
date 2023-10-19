import numpy as np

a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])

print('数组 a：')
print(a)
ainv = np.linalg.inv(a)

print('a 的逆：')
print(ainv)

print('矩阵 b：')
b = np.array([[6], [-4], [27]])
print(b)

print('计算：A^(-1)B：')
x = np.linalg.solve(a, b)
print(x)
# 这就是线性方向 x = 5, y = 3, z = -2 的解
