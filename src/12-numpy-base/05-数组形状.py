import numpy as np

if __name__ == '__main__':
    # 数组的形状是每个维中元素的数量。
    # 上面的例子返回(2, 4)，这意味着该数组有 2 个维，每个维有 4 个元素。
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr.shape)
