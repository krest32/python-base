import numpy as np

# ndarray.view() 方会创建一个新的数组对象，
# 该方法创建的新数组的维数变化不会改变原始数据的维数。
# 最开始 a 是个 3X2 的数组
a = np.arange(6).reshape(3, 2)
print('数组 a：')
print(a)
print('创建 a 的视图：')
b = a.view()
print(b)

print('两个数组的 id() 不同：')
print('a 的 id()：')
print(id(a))
print('b 的 id()：')
print(id(b))

# 修改 b 的形状，并不会修改 a
b.shape = 2, 3
print('b 的形状：')
print(b)
print('a 的形状：')
print(a)
