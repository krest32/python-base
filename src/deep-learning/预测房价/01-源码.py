import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# 加载数据
def load_data(filename):
    train_data = pd.read_csv(filename)
    # insert 第一个参数：索引，第二个参数：列名，第三个参数：值
    train_data.insert(0, 'Ones', 1)
    # 获取数据的第一列和第二列
    x = train_data.iloc[:, [0, 1]]
    # 获取数据的第三列
    y = train_data.iloc[:, 2]
    # 返回数据
    return x.values, y.values


# 梯度下降法
def gradient_descent(X, Y, Theta, alpha, iters):
    m = len(Y)
    # 展示用来存放 w,b 两个一次函数的参数
    temp = np.zeros(Theta.shape)

    cols = len(Theta)
    # 定义了一对的 0？
    costs = np.zeros(iters)
    # 循环 iters 次
    for i in range(iters):
        # 计算得到 预期点与 实际点之间的距离
        dis = X @ Theta - Y
        # 计算 w, b 两个参数的值
        for j in range(cols):
            term = dis * X[:, j]
            temp[j] = Theta[j] - alpha * np.sum(term) / m
        Theta = temp
        # 计算最后的损失 J
        costs[i] = cost_function(X, Y, Theta)
    # 得到 w,b 两个参数，以及损失值 J
    return Theta, costs


# 损失函数值求取
def cost_function(X, Y, Theta):
    m = len(Y)
    # 计算预期与实际结果的平方差
    inner = np.power((X @ Theta - Y), 2)
    # 然后得到除以 1/2m 得到损失值 J
    return np.sum(inner) / (2 * m)


# 线性回归
def linear_regression(predict_year):
    # 加载数据
    X, Y = load_data('data.csv')
    # 原数据减去 2000 方便进行计算
    X[:, 1] -= 2000

    # 梯度下降初始的 w, b 两个参数
    theta = np.array([0, 0])

    # 设置迭代次数
    iters = 3000
    # 定义 学习律/步长
    alpha = 0.0001

    w, costs = gradient_descent(X, Y, theta, alpha, iters)
    print("w:", w)
    # 说是函数的值
    print("cost:", costs)


    x = np.arange(0, 20, 2)

    f = w[0] + w[1] * x
    p_year = predict_year - 2000
    p_price = w[0] + w[1] * p_year
    x_ticks = x + 2000
    plt.xticks(x_ticks)
    plt.xlabel('Year')
    plt.ylabel('price')
    plt.title('Price of house')
    plt.scatter(X[:, 1] + 2000, Y, color='red')
    plt.scatter(predict_year, p_price, color='green')
    plt.plot(x_ticks, f)

    plt.figure()
    plt.title('Cost')
    plt.xlabel('iterations')
    plt.ylabel('cost')
    plt.plot(costs)
    plt.show()


if __name__ == '__main__':
    # 预测 2024 年的房价
    linear_regression(2024)
