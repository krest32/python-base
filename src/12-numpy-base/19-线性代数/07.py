import numpy as np

b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(b)

print(np.linalg.det(b))
print(6 * (-2 * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - -2 * 2))
