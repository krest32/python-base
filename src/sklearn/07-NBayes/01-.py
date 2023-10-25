import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()
from sklearn.datasets import make_blobs

# make_blobs：为聚类产生数据集
# n_samples：样本点数，n_features：数据的维度，centers:产生数据的中心点，默认值3
# cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0，random_state：随机种子
X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
plt.show()
