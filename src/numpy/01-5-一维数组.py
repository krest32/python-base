import numpy
import numpy as np

if __name__ == '__main__':
    a1 = np.array([1, 2, 3])
    print(a1)

    a2 = np.zeros(3, int)
    print(a2)

    a3 = np.zeros_like(a2)
    print(a3)

    # 宽度为3 填充7
    a4 = np.full(3, 7)
    print(a4)

    # 填充空数组3个随机的浮点数
    a5 = np.empty(3)
    print(a5)

    # 从 0 开始到 6
    a6 = np.arange(6)
    print(a6)

    # 从2到6步长2
    a7 = np.arange(2, 6, 2)
    print(a7)

    # 访问数据
    b = np.arange(1, 6)
    print(b)
    # 获取下标1的元素
    print(b[1])
    # 从2到4，不包含4
    print(b[2:4])
    # 访问最后两个元素
    print(b[-2:])
    # ，所以意思就是从开始到结束，每n个取一个值。
    print(b[::2])
    print(b[::3])
    # 访问指定下标数据
    print(b[[1, 3, 4]])
    # 根据 bool 获取元素
    print(b[b > 2])

    # 两个特殊函数
    b1 = np.where(b > 2)
    print(b1)

    # 复制
    c = b.copy();
    print(c)

    # 计算
    d = np.array([[1, 2]])

    # 平方
    d1 = d ** 2
    print(d1)

    # 根号下
    d2 = np.sqrt(d1)
    print(d2)

    # e的数组次平方
    d3 = np.exp(d2)
    print(d3)

    # 求取对数
    d4 = np.log(d2)
    print(d4)

    # 向量乘积-点乘
    e1 = np.array([1, 2])
    e2 = np.array([3, 4])
    e3 = np.dot(e1, e2)
    print(e3)
    # 向量乘积-叉乘
    e5 = np.array([2, 0, 0])
    e6 = np.array([0, 3, 0])
    e4 = np.cross(e5, e6)
    print(e4)
