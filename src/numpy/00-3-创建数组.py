import numpy as np

if __name__ == '__main__':
    # numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
    x1 = np.empty([3, 2], dtype=int)
    print(x1)

    # 创建指定大小的数组，数组元素以 0 来填充：
    # 默认为浮点数
    x2 = np.zeros(5)
    print(x2)

    # 设置类型为整数
    y1 = np.zeros((5,), dtype=int)
    print(y1)

    # 自定义类型
    z1 = np.zeros((2, 2), dtype=[
        ('x', 'i4'),
        ('y', 'i4')
    ])
    print(z1)

    # 创建指定形状的数组，数组元素以 1 来填充：
    # numpy.ones(shape, dtype = None, order = 'C')
    # 默认为浮点数
    x3 = np.ones(5)
    print(x3)

    # 自定义类型
    x4 = np.ones([2, 2], dtype=int)
    print(x4)

    # numpy.zeros_like
    # numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充。
    # 创建一个 3x3 的二维数组
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # 创建一个与 arr 形状相同的，所有元素都为 0 的数组
    zeros_arr = np.zeros_like(arr)
    print(zeros_arr)