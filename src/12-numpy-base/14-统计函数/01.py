# numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
# a: 输入的数组，可以是一个NumPy数组或类似数组的对象。
# axis: 可选参数，用于指定在哪个轴上计算最大值。如果不提供此参数，则返回整个数组的最大值。可以是一个整数表示轴的索引，也可以是一个元组表示多个轴。
# out: 可选参数，用于指定结果的存储位置。
# keepdims: 可选参数，如果为True，将保持结果数组的维度数目与输入数组相同。如果为False（默认值），则会去除计算后维度为1的轴。
# initial: 可选参数，用于指定一个初始值，然后在数组的元素上计算最大值。
# where: 可选参数，一个布尔数组，用于指定仅考虑满足条件的元素。

import numpy as np

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('我们的数组是：')
print(a)

print('调用 amin() 函数：')
print(np.amin(a, 1))

print('再次调用 amin() 函数：')
print(np.amin(a, 0))

print('调用 amax() 函数：')
print(np.amax(a))

print('再次调用 amax() 函数：')
print(np.amax(a, axis=0))
