import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB

sns.set()
from sklearn.datasets import make_blobs

# make_blobs：为聚类产生数据集
# n_samples：样本点数，n_features：数据的维度，centers:产生数据的中心点，默认值3
# cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0，random_state：随机种子
X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=2, cluster_std=1.5)

model = GaussianNB()  # 朴素贝叶斯
model.fit(X, y)
rng = np.random.RandomState(0)
X_test = [-6, -14] + [14, 18] * rng.rand(5000, 2)  # 生成测试集
y_pred = model.predict(X_test)
# 将训练集和测试集的数据用图像表示出来，颜色深直径大的为训练集，颜色浅直径小的为测试集
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
lim = plt.axis()  # 获取当前的坐标轴限制参数
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, s=20, cmap='RdBu', alpha=0.1)
plt.axis(lim)
plt.show()

yprob = model.predict_proba(X_test)
print(yprob[:20].round(2))

