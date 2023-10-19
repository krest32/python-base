import numpy as np

x = np.arange(9.).reshape(3, 3)
print('我们的数组是：')
print(x)
# 定义条件, 选择偶数元素
condition = np.mod(x, 2) == 0
print('按元素的条件值：')
print(condition)
print('使用条件提取元素：')
print(np.extract(condition, x))