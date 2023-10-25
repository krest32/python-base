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



plt.figure(figsize=(16, 15))

# 画出多个多项式等级来对比
for i, degree in enumerate([1, 3, 5, 7, 9, 12]):
    model_poly = svm.SVC(C=0.001, kernel='poly', degree=degree)  # 多项式核
    model_poly.fit(data, label)
    Z = model_poly.predict(np.c_[xx.ravel(), yy.ravel()])  # 预测
    Z = Z.reshape(xx.shape)

    plt.subplot(3, 2, i + 1)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)  # 调整子图的间距
    plt.contourf(xx, yy, Z, cmap=plt.cm.ocean, alpha=0.6)

    plt.scatter(data[:6, 0], data[:6, 1], marker='o', color='r', s=100, lw=3)
    plt.scatter(data[6:, 0], data[6:, 1], marker='x', color='k', s=100, lw=3)
    plt.title('Poly SVM with $\degree=$' + str(degree))

plt.show()
