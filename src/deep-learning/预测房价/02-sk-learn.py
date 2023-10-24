import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# 创建虚拟数据
def create_data():
    x = np.array(range(30))
    temp_y = 10 + 2 * x + x ** 2 + x ** 3
    y = temp_y + 1500 * np.random.normal(size=30)  # 添加噪声
    x = x.reshape(30, 1)
    y = y.reshape(30, 1)
    print(x)
    print(y)
    return x, y


def linear_regression(x, y):
    # 调用线性回归
    clf1 = LinearRegression()
    # 加入数据，调试模型
    clf1.fit(x, y)
    return clf1


def un_linear_regression(x, y):
    # 非线性回归
    # 根据degree的值转换为相应的多项式（非线性回归），也就是几级的 泰勒多项式
    ploy_feat = PolynomialFeatures(degree=4)
    x_p = ploy_feat.fit_transform(x)
    clf2 = LinearRegression()
    clf2.fit(x_p, y)
    return clf2, x_p
# 手寫非线性回归方程 3阶泰勒展开
def test_func(clf2, x):
    return clf2.intercept_[0] + clf2.coef_[0, 1] * (x ** 1) + clf2.coef_[0, 2] * (x ** 2) + clf2.coef_[0, 3] * (x ** 3)


if __name__ == '__main__':
    x, y = create_data()
    clf1 = linear_regression(x, y)

    clf2, x_p = un_linear_regression(x, y)
    print("线性回归方程为: y = {} + {}x".format(clf1.intercept_[0], clf1.coef_[0, 0]))
    print("非线性回归曲线方程为 y = {}+{}x+{}x^2+{}x^3".format(clf2.intercept_[0], clf2.coef_[0, 1], clf2.coef_[0, 2],
                                                               clf2.coef_[0, 3]))
    font = {"family": "FangSong", 'size': 12}
    matplotlib.rc("font", **font)
    # 线性回归预测值
    y_l = clf1.predict(x)
    plt.plot(x, clf2.predict(x_p), label="非线性回归_调用预测")
    plt.plot(x, y_l, label="线性回归_调用预测")
    plt.scatter(x, y, label="数据")
    plt.legend()
    plt.show()
    print(test_func(clf2, 30))


