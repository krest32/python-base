import numpy
import numpy as np

if __name__ == '__main__':
    # 二维数组
    a1 = np.array([
        [1, 2, 3],
        [2, 3, 4]
    ])
    print(a1)

    print(np.zeros((3, 2)))
    print(np.full((3, 2), 7))
    print(np.ones((3, 2)))
    print(np.empty((3, 2)))
    print("----------------------------")

    # 二维随机数组
    # 0-10, 3*2 随机数组
    print(np.random.randint(0, 10, [3, 2]))
    # 0-1 浮点数, 3*2 随机数组
    print(np.random.rand(3, 2))
    # 0-10 浮点数， 3*2 随机数组
    print(np.random.uniform(1, 10, [3, 2]))
    print("-------------------------------")

    # 二维数组索引
    c = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print(c)
    # 第2行，第3列
    print(c[1, 2])
    # 第2行
    print(c[1, :])
    # 第3列
    print(c[:, 2])
    # 第2,3列
    print(c[:, 1:3])
    # 倒数第2行，第二列
    print(c[-2:, -2:])
    # 间隔为2 (稍微有点看不懂)
    print(c[::2, 1::2])
    print("-------------------------------------")

    # 轴参数
    d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    # 每项相加
    print(d.sum())
    # 求取每一列的和
    print(d.sum(axis=0))
    # 求取每一行的和
    print(d.sum(axis=1))
    print("------------------------------------")

    # 矩阵变形
    e = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print(e)
    print(e.T)

    f = np.array([1, 2, 3, 4, 5, 6])
    print(f)
    print(f.reshape(2, 3))
    print("--------------------------------------")

    # 矩阵拼接
    g1 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    g2 = np.array([
        [1, 2],
        [3, 4],
        [5, 6]
    ])
    g3 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ])
    # 拼接在右边
    print(np.hstack((g1, g2)))
    # 等同于 np.hstack
    # print(np.column_stack((g1, g2)))
    # 拼接在底部
    print(np.vstack((g1, g3)))
    print("---------------------------")

    # 矩阵拆分
    h1 = np.array([
        [1, 2, 3, 4, 1, 2],
        [4, 5, 6, 7, 4, 5],
        [8, 9, 0, 10, 8, 9]
    ])
    # 垂直拆分
    print(np.hsplit(h1, [4]))
    # 水平拆分
    print(np.vsplit(h1, [2]))
    print("------------------------------")

    # 矩阵复制
    # tile 类似粘贴复制；
    # repeat 相当于分页打印。
    i = np.array([
        [1, 2],
        [3, 4]
    ])

    print(np.tile(i, (2, 3)))
    print(i.repeat(3, axis=1))
    print(i.repeat(3, axis=0))

    # 删除
    j = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    # 删除第1,3列
    print(np.delete(j, [1, 3], axis=1))
    # 删除第2行
    print(np.delete(j, 1, axis=0))
    # 保留首尾
    print(np.delete(j, slice(1, -1), axis=1))
    print("------------------------------")

    # 插入数据
    k = np.array([
        [1, 2, 3, 4, 5, 6],
        [8, 9, 10, 11, 12, 13]
    ])
    print(np.insert(k, 1, 7, axis=0))

    k2 = np.array([
        [7, 7],
        [7, 7]
    ])
    # 插入已知的数列
    print(np.insert(k, [1], k2, axis=1))
    print("-----------------------------------")

    # append
    l = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])

    # 统计
    j = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 1]
    ])
    # 矩阵最小值
    print(j.min())
    print(j.min(axis=1))
    print(j.min(axis=0))

    #
    print(j.argmin())