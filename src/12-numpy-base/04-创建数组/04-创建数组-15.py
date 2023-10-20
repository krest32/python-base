import numpy as np

# 以下实例设置间距。
a = np.linspace(1, 10, 10, retstep=True)
print(a)
# 拓展例子
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)
