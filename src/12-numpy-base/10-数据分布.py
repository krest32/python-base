import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 创建一个包含 100000 个介于 0 到 5 之间的随机浮点数的数组：
    # 并使用具有 100 栏的直方图显示它们
    x = numpy.random.uniform(0.0, 5.0, 100000)

    plt.hist(x, 100)
    plt.show()
