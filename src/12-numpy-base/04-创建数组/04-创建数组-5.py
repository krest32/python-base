import numpy as np

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)
