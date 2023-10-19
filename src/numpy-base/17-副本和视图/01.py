import numpy as np

a = np.arange(6)
print('我们的数组是：')
print(a)

print('调用 id() 函数：')
print(id(a))
print('a 赋值给 b：')

b = a
print(b)
print('b 拥有相同 id()：')
print(id(b))
print('修改 b 的形状：')

b.shape = 3, 2
print(b)
print('a 的形状也修改了：')
print(a)