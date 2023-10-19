import numpy as np

arr = np.arange(12)
print('我们的数组：')
print(arr)
print('创建切片：')
a = arr[3:]
b = arr[3:]
a[1] = 123
b[2] = 234
print(arr)
print(id(a), id(b), id(arr[3:]))