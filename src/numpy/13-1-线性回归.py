import matplotlib.pyplot as plt
from scipy import stats


def func1():
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    plt.scatter(x, y)
    plt.show()


def func2():
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    # 执行一个方法，该方法返回线性回归的一些重要键值：
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    # 创建一个使用 slope 和 intercept 值的函数返回新值。这个新值表示相应的 x 值将在 y 轴上放置的位置：
    # R-Squared
    # 重要的是要知道 x 轴的值和 y 轴的值之间的关系有多好，如果没有关系，则线性回归不能用于预测任何东西。
    # 该关系用一个称为 r 平方（r-squared）的值来度量
    # r 平方值的范围是 0 到 1，其中 0 表示不相关，而 1 表示 100％ 相关。
    # Python 和 Scipy 模块将为您计算该值，您所要做的就是将 x 和 y 值提供给它：
    def myfunc(x):
        return slope * x + intercept

    # 通过函数运行 x 数组的每个值。这将产生一个新的数组，其中的 y 轴具有新值：
    mymodel = list(map(myfunc, x))

    # 绘制原始散点图：
    plt.scatter(x, y)
    # 绘制线性回归线：
    plt.plot(x, mymodel)
    plt.show()


if __name__ == '__main__':
    # 在下面的示例中，x 轴表示车龄，y 轴表示速度。我们已经记录了 13 辆汽车通过收费站时的车龄和速度。让我们看看我们收集的数据是否可以用于线性回归：
    # func1()
    # 导入 scipy 并绘制线性回归线：
    func2()
