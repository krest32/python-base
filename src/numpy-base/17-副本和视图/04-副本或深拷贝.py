import numpy as np

a = np.array([[10, 10], [2, 3], [4, 5]])
print('数组 a：')
print(a)
print('创建 a 的深层副本：')
b = a.copy()
print('数组 b：')
print(b)

# b 与 a 不共享任何内容
print('我们能够写入 b 来写入 a 吗？')
print(b is a)
print('修改 b 的内容：')
b[0, 0] = 100
print('修改后的数组 b：')
print(b)
print('a 保持不变：')
print(a)