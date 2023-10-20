import numpy as np

# np.ix_ 函数就是输入两个数组，产生笛卡尔积的映射关系。
# 笛卡尔乘积是指在数学中，两个集合 X 和 Y 的笛卡尔积（Cartesian product），又称直积，表示为 X×Y，
# 第一个对象是X的成员而第二个对象是 Y 的所有可能有序对的其中一个成员。
x = np.arange(32).reshape((8, 4))
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
