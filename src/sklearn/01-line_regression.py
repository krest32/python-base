import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# 设定一个真实函数
def true_fun(x):
    return 1.5 * x + 0.2


# 设置一个随机种子, 也就是一个开始值
np.random.seed(0)
# 设置样本数量为 50
n_samples = 50

# 生成一个数据作为训练集
x_train = np.sort(np.random.rand(n_samples))
# 并且增加一些噪声
y_train = (true_fun(x_train) + np.random.rand(n_samples) * 0.2).reshape(n_samples, 1)


# 这就是我们的模型
model = LinearRegression()
# 训练模型
# X_train是一个一维的向量，那么其作用就是将X_train变成一个N*1的二维矩阵而已。其实写成 X_train[:,None] 是相同的效果。
model.fit(x_train[:, np.newaxis], y_train)
print("输出参数w：", model.coef_)
print("输出参数b：", model.intercept_)

# 0 和 1 之间，产生 100 个等间距的
x_test = np.linspace(0, 1, 100)
# 将拟合出来的散点画出
plt.plot(x_test, model.predict(x_test[:, np.newaxis]), label="Model")
plt.plot(x_test, true_fun(x_test), label="True function")  # 真实结果
# 画出训练集的点
plt.scatter(x_train, y_train)
plt.legend(loc="best")  # 将标签放在最合适的位置
plt.show()
