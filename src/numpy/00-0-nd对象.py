import numpy as np
if __name__ == '__main__':
    # 一维数组
    a1 = np.array([1,2,3])
    print (a1)

    # 二维数组
    a2 = np.array([[1, 2], [3, 4]])
    print(a2)

    # 最小维度
    a3 = np.array([1, 2, 3, 4, 5], ndmin=2)
    print(a3)

    # dtype 参数
    a4 = np.array([1, 2, 3], dtype=complex)
    print(a4)