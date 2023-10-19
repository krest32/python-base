import numpy as np

a = np.array([1, 256, 8755], dtype=np.int16)
print('我们的数组是：')
print(a)
print('以十六进制表示内存中的数据：')
print(map(hex, a))
# byteswap() 函数通过传入 true 来原地交换
print('调用 byteswap() 函数：')
print(a.byteswap(True))
print('十六进制形式：')
print(map(hex, a))
# 我们可以看到字节已经交换了