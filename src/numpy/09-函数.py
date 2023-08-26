import numpy as np

if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [4, 5, 6, 7]
    z = []

    # 一种方法是遍历两个列表，然后对每个元素求和。
    for i, j in zip(x, y):
        z.append(i + j)
    print(z)

    x = [1, 2, 3, 4]
    y = [4, 5, 6, 7]
    v = [4, 5, 6, 7]
    z = np.add(x, y)
    k = np.add(v, z)

    print(k)
