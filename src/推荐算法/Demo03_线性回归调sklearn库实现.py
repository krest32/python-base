import numpy as np
import matplotlib.pyplot as plt


points = np.genfromtxt('data.csv', delimiter=',')

points[0,0]

# 提取points中的两列数据，分别作为x，y
x = points[:, 0]
y = points[:, 1]

# 用plt画出散点图
plt.scatter(x, y)
# plt.show()


from sklearn.linear_model import LinearRegression
lr = LinearRegression()

# 行程一个新的矩阵（n行，一列）
x_new = x.reshape(-1, 1)
y_new = y.reshape(-1, 1)
lr.fit(x_new, y_new)


# 从训练好的模型中提取系数和截距
w = lr.coef_[0][0]
b = lr.intercept_[0]

print("w is: ", w)
print("b is: ", b)

# 针对每一个x，计算出预测的y值
pred_y = w * x + b
plt.plot(x, pred_y, c='r')
plt.show()