import numpy as np

a = np.array([1, 2, 3, 4])
print('我们的数组是：')
print(a)

print('调用 average() 函数：')
print(np.average(a))

# 不指定权重时相当于 mean 函数
wts = np.array([4, 3, 2, 1])
print('再次调用 average() 函数：')
print(np.average(a, weights=wts))

# 如果 returned 参数设为 true，则返回权重的和
print('权重的和：')
print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))