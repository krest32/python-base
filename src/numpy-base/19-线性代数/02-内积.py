import numpy as np

# 1*11 + 2*12 + 3*13 + 4*14 = 130
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])

# vdot 将数组展开计算内积
print(np.vdot(a, b))