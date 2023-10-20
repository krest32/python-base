import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3, 10])

# 如果我们不指定 x 轴上的点，则 x 会根据 y 的值来设置为 0, 1, 2, 3..N-1。
plt.plot(ypoints)
plt.show()