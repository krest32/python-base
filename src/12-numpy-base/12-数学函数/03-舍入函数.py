import numpy as np

# decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print('原数组：')
print(a)

print('舍入后：')
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))
