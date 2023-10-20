import numpy as np

# [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b))