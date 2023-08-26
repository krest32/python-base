import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
    # NumPy 有一种方法可以让我们建立多项式模型：
    mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
    # 然后指定行的显示方式，我们从位置 1 开始，到位置 22 结束：
    myline = numpy.linspace(1, 22, 100)
    # 绘制原始散点图：
    plt.scatter(x, y)
    # 画出多项式回归线：
    plt.plot(myline, mymodel(myline))
    plt.show()
