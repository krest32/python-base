# numpy.percentile()
# 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。 函数numpy.percentile()接受以下参数。
#
# numpy.percentile(a, q, axis)
# 参数说明：
#
# a: 输入数组
# q: 要计算的百分位数，在 0 ~ 100 之间
# axis: 沿着它计算百分位数的轴


import numpy as np

a = np.array([[10, 7, 4], [3, 2, 1]])
print('我们的数组是：')
print(a)

print('调用 percentile() 函数：')
# 50% 的分位数，就是 a 里排序之后的中位数
print(np.percentile(a, 50))

# axis 为 0，在纵列上求
print(np.percentile(a, 50, axis=0))

# axis 为 1，在横行上求
print(np.percentile(a, 50, axis=1))

# 保持维度不变
print(np.percentile(a, 50, axis=1, keepdims=True))