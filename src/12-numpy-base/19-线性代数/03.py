import numpy as np

# numpy.inner() 函数返回一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积。
print(np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))
# 等价于 1*0+2*1+3*0