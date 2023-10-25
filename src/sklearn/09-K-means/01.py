from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from sklearn import datasets

# 聚类前
X = np.random.rand(1000, 2)
plt.scatter(X[:, 0], X[:, 1], marker='o')
plt.show()


# 初始化质心，从原有数据中挑选k个作为质心
def IiniCentroids(X, k):
    index = np.random.randint(0, len(X) - 1, k)
    return X[index]


# 聚类后
kmeans = KMeans(n_clusters=4)  # 分成2类
kmeans.fit(X)
label_pred = kmeans.labels_
plt.scatter(X[:, 0], X[:, 1], c=label_pred)
plt.show()

print("聚类中心为：",kmeans.cluster_centers_)
print("评估：",kmeans.inertia_)

