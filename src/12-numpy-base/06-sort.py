import numpy as np

if __name__ == '__main__':
    arr = np.array([3, 2, 0, 1])
    print(np.sort(arr))

    # 二维数组
    arr = np.array([
        [3, 2, 4],
        [5, 0, 1]
    ])
    print(np.sort(arr))
