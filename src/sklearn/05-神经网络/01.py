from sklearn.neural_network import MLPClassifier
from sklearn.datasets import fetch_openml
import numpy as np

# 那么还有一些值得注意的参数为：
#
# activation：选择激活函数，可选有{‘identity’,‘logistic’,‘tanh’,‘relu’}，默认为relu
# solver：权重优化器，可选有{‘lbfgs’,‘sgd’,‘adam’}，默认为adam
# learning_rate_init：初始学习率，仅在sgd或者adam时使用


mnist = fetch_openml("mnist_784", parser='auto')  # 加载数据集
X, y = mnist['data'], mnist['target']
X_train = np.array(X[:60000], dtype=float)
y_train = np.array(y[:60000], dtype=float)
X_test = np.array(X[60000:], dtype=float)
y_test = np.array(y[60000:], dtype=float)

clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(15, 15), random_state=1)
# alpha为正则项的惩罚系数，第二个为每一层隐藏节点的个数，这里就是2层，每层15个

clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)
print(score)
