import numpy as np

# 传入倒序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[-4, -2, -1, -7]])
