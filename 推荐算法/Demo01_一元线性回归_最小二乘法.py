# 读取文件依赖
import numpy as np
# 画图依赖
import matplotlib.pyplot as plt

#
points = np.genfromtxt('data.csv', delimiter=',')
x = points[:, 0]
y = points[:, 1]


# 打印散列图
# plt.scatter(x, y)
# plt.show()


# 定义一个拟合函数
def average(data):
    sum = 0
    num = len(data)
    for i in range(num):
        sum += data[i]
    return sum / num


def fit(points):
    M = len(points)
    x_bar = average(points[:, 0])
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        sum_yx += y * (x - x_bar)
        sum_x2 += x ** 2

    # 计算 w
    w = sum_yx / (sum_x2 - M * (x_bar ** 2))
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        sum_delta += (y - w * x)
    b = sum_delta / M
    return w, b


# 计算损失函数， 另外传入数据的 w b x y
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        #  平方 **2 即可
        total_cost += (y - w * x - b) ** 2
    return total_cost / M


w, b = fit(points)
print("w is :", w)
print("b is :", b)

cost = compute_cost(w, b, points)
print("cost is:", cost)

# w is : 1.3224310227553846
# b is : 7.991020982269173
# cost is: 110.25738346621313

# 画图
plt.scatter(x, y)
pred_y = w * x + b
plt.plot(x, pred_y, c='r')
plt.show()