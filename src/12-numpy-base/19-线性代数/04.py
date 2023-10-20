import numpy as np

a = np.array([[1, 2], [3, 4]])

print('数组 a：')
print(a)
b = np.array([[11, 12], [13, 14]])

print('数组 b：')
print(b)

print('内积：')
print(np.inner(a, b))

# 1*11+2*12, 1*13+2*14
# 3*11+4*12, 3*13+4*14