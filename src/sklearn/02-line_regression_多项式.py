import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures  # 导入能够计算多项式特征的类
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score  # 交叉验证


# 真实函数
def true_fun(X):
    return np.cos(1.5 * np.pi * X)


# 模拟样本数据
np.random.seed(0)
n_samples = 30

# 随机采样后排序
X = np.sort(np.random.rand(n_samples))
# 生成随机训练数据
y = true_fun(X) + np.random.randn(n_samples) * 0.1

# 多项式最高次，我们分别用1次，4次和15次的多项式来尝试拟合
degrees = [1, 4, 15]
plt.figure(figsize=(14, 5))

for i in range(len(degrees)):
    # 总共三个图，获取第i+1个图的图像柄
    ax = plt.subplot(1, len(degrees), i + 1)
    # 这是设置ax图中的属性
    plt.setp(ax, xticks=(), yticks=())
    # 建立多项式回归的类，第一个参数就是多项式的最高次数，第二个是是否包含偏置
    polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
    # 线性回归
    linear_regression = LinearRegression()
    # 使用pipline串联模型
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("linear_regression", linear_regression)])
    # x 转换为 二维数组， 输入训练集
    pipeline.fit(X[:, np.newaxis], y)
    scores = cross_val_score(pipeline, X[:, np.newaxis], y, scoring="neg_mean_squared_error", cv=10)
    # 使用交叉验证，第一个参数为模型，第二个为输入，第三个为标签，第四个为误差计算方式，第五个为多少折
    X_test = np.linspace(0, 1, 100)
    # 预测数据
    plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Model")
    # 真实数据
    plt.plot(X_test, true_fun(X_test), label="True function")
    # 样本点描绘
    plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc="best")
    plt.title("Degree {}\nMSE = {:.2e}(+/- {:.2e})".format(degrees[i], -scores.mean(), scores.std()))

plt.show()
