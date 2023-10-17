import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 预测未来值
    # 现在，我们可以使用收集到的信息来预测未来的值。
    # 例如：让我们尝试预测在晚上 17 点左右通过收费站的汽车的速度：
    # 为此，我们需要与上面的实例相同的 mymodel 数组：
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

    my_model = numpy.poly1d(numpy.polyfit(x, y, 3))

    speed = my_model(17)
    print(speed)
