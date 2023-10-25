import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

data = np.array([
    [0.1, 0.7],
    [0.3, 0.6],
    [0.4, 0.1],
    [0.5, 0.4],
    [0.8, 0.04],
    [0.42, 0.6],
    [0.9, 0.4],
    [0.6, 0.5],
    [0.7, 0.2],
    [0.7, 0.67],
    [0.27, 0.8],
    [0.5, 0.72]
])  # 建立数据集
label = [1] * 6 + [0] * 6  # 前6个数据的label为1，后6个为0
x_min, x_max = data[:, 0].min() - 0.2, data[:, 0].max() + 0.2
y_min, y_max = data[:, 1].min() - 0.2, data[:, 0].max() + 0.2
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.002),
                     np.arange(y_min, y_max, 0.002))  # 生成网格网络
model_linear = svm.SVC(kernel='linear', C=0.001)  # 线性SVM模型
model_linear.fit(data, label)
Z = model_linear.predict(np.c_[xx.ravel(), yy.ravel()])
# 是先将xx（size*size）和yy(size*size)拉成一维，然后让它们相连，成为一个两列的矩阵，然后作为X进去预测
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.ocean, alpha=0.6)
# 可以理解为绘制等高线，xx为横坐标，yy为轴坐标，Z为确切坐标点的取值，cmap为配色方案
plt.scatter(data[:6, 0], data[:6, 1], marker='o', color='r', s=100, lw=3)
plt.scatter(data[6:, 0], data[6:, 1], marker='x', color='k', s=100, lw=3)
plt.title("Linear SVM")
plt.show()
