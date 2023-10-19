import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    # 我们使用 numpy.random.normal() 方法创建的数组（具有 100000 个值）绘制具有 100 栏的直方图。
    # 我们指定平均值为 5.0，标准差为 1.0。
    # 这意味着这些值应集中在 5.0 左右，并且很少与平均值偏离 1.0。
    # 从直方图中可以看到，大多数值都在 4.0 到 6.0 之间，最高值大约是 5.0。
    x = numpy.random.normal(5.0, 1.0, 100000)
    plt.hist(x, 100)
    plt.show()
