import seaborn as sns
from pandas import plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

# 加载数据集
data = load_iris()
# 转换成DataFrame的格式
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Species'] = data.target  # 添加品种列
# 查看数据集信息
print(f"数据集信息：\n{df.info()}")
# 查看前5条数据
print(f"前5条数据：\n{df.head()}")
df.describe()


# 用数值代替品类名称
target = np.unique(data.target)  # 去重
print(target)
target_names = np.unique(data.target_names)
print(target_names)
targets = dict(zip(target, target_names))
print(targets)
df['Species'] = df['Species'].replace(targets)

# 提取数据和标签
X =df.drop(columns = 'Species')  # 把标签列丢掉就是特征
y = df['Species']
feature_names = X.columns
labels = y.unique()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)
# 划分训练集与测试集，测试集比例为0.4，随机种子为42
model = DecisionTreeClassifier(max_depth = 3, random_state = 42)  # 决策树的最大深度为3
model.fit(X_train, y_train)
# 以文字的形式输出树
text_representation = tree.export_text(model)
print(text_representation)

# 以图片的形式画出
plt.figure(figsize=(30, 10), facecolor='w')
a = tree.plot_tree(model,
                  feature_names = feature_names,
                  class_names = labels,
                  rounded = True,
                  filled = True,
                  fontsize = 14)
plt.show()