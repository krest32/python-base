import numpy as np

#  输出下表为 4, 2, 1, 7 对应的行，输出结果为：
x = np.arange(32).reshape((8, 4))
print(x)
# 二维数组读取指定下标对应的行
print("-------读取下标对应的行-------")
print(x[[4, 2, 1, 7]])
