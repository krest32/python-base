import numpy as np

print(np.matlib.empty((2, 2)))
# 填充为随机数据

print (np.zeros((2,2)))


print (np.matlib.ones((2,2)))


# numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))

# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))

# numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
print (np.matlib.rand(3,3))