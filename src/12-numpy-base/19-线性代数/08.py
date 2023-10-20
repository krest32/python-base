import numpy as np

# numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵。
# 逆矩阵（inverse matrix）：
#   设A是数域上的一个n阶矩阵，若在相同数域上存在另一个n阶矩阵B，
#   使得： AB=BA=E ，则我们称B是A的逆矩阵，而A则被称为可逆矩阵。
#   注：E为单位矩阵。
x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))
