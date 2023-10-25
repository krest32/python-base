import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

wine = load_wine()  # 使用葡萄酒数据集
print(f"所有特征：{wine.feature_names}")
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 构造并训练决策树分类器
base_model = DecisionTreeClassifier(max_depth=1, criterion='gini', random_state=1)
# 使用基尼指数作为选择标准
base_model.fit(X_train, y_train)
y_pred = base_model.predict(X_test)
model = RandomForestClassifier(n_estimators=50,
                               random_state=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"RandomForestClassifier的准确率：{accuracy_score(y_test, y_pred):.3f}")

x = list(range(2, 102, 2))  # 估计器个数即n_estimators，在这里我们取[2,102]的偶数
y = []

for i in x:
    model = RandomForestClassifier(
        n_estimators=i,

        random_state=1)

    model.fit(X_train, y_train)
    model_test_sc = accuracy_score(y_test, model.predict(X_test))
    y.append(model_test_sc)

plt.style.use('ggplot')
plt.title("Effect of n_estimators", pad=20)
plt.xlabel("Number of base estimators")
plt.ylabel("Test accuracy of RandomForestClassifier")
plt.plot(x, y)
plt.show()
