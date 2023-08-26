import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Matplotlib 模块有一种绘制散点图的方法，
    # 它需要两个长度相同的数组，一个数组用于 x 轴的值，另一个数组用于 y 轴的值：
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    plt.scatter(x, y)
    plt.show()
