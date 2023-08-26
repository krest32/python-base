import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
# 训练/测试是一种测量模型准确性的方法。
# 之所以称为训练/测试，是因为我们将数据集分为两组：训练集和测试集。
# 80％ 用于训练，20％ 用于测试。
# 您可以使用训练集来训练模型。
# 您可以使用测试集来测试模型。
# 训练模型意味着创建模型。
# 测试模型意味着测试模型的准确性。
if __name__ == '__main__':
    numpy.random.seed(2)

    x = numpy.random.normal(3, 1, 100)
    y = numpy.random.normal(150, 40, 100) / x

    # x 轴表示购买前的分钟数。
    # y 轴表示在购买上花费的金额。
    plt.scatter(x, y)
    plt.show()

    # 训练集应该是原始数据的 80％ 的随机选择。
    # 测试集应该是剩余的 20％。
    train_x = x[:80]
    train_y = y[:80]

    test_x = x[80:]
    test_y = y[80:]

    # 显示与训练集相同的散点图：
    plt.scatter(train_x, train_y)
    plt.show()

    # 显示测试集
    plt.scatter(test_x, test_y)
    plt.show()

    # 数据集是什么样的？我认为最合适拟合的是多项式回归，因此让我们画一条多项式回归线。
    # 要通过数据点画一条线，我们使用 matplotlib 模块的 plott() 方法：
    # 实例
    mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
    myline = numpy.linspace(0, 6, 100)
    plt.scatter(train_x, train_y)
    plt.plot(myline, mymodel(myline))
    plt.show()

    r2 = r2_score(test_y, mymodel(test_x))
    print(r2)
    # 注释：结果 0.809 表明该模型也适合测试集，我们确信可以使用该模型预测未来值。

    # 现在我们已经确定我们的模型是不错的，可以开始预测新值了。
    # 如果购买客户在商店中停留 5 分钟，他/她将花费多少钱？
    print(mymodel(5))