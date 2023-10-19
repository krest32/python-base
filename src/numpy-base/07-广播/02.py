import numpy as np

# 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。如：
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([0, 1, 2])
print(a + b)
