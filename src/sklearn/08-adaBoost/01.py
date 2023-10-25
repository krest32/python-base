from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

wine = load_wine()#使用葡萄酒数据集
print(f"所有特征：{wine.feature_names}")
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

base_model = DecisionTreeClassifier(max_depth = 1, criterion='gini', random_state = 1)
base_model.fit(X_train, y_train)
y_pred = base_model.predict(X_test)
print(f"决策树的准确率：{accuracy_score(y_test,y_pred):.3f}")


# 那么接下来我们尝试应用AdaBoost算法来拟合：
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV
model = AdaBoostClassifier(base_estimator=base_model, n_estimators=50, learning_rate = 0.8)
# n_estimators和learning_rate是要调的参数，lr是弱学习器的权重衰减系数
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred) # 准确率
print(f"准确率：{acc:.2}")


hyperparameter_space = {"n_estimators":list(range(2,102,2)),
                       "learning_rate":[0,1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]}
gs = GridSearchCV(AdaBoostClassifier(algorithm='SAMME.R', random_state = 1),
                 param_grid = hyperparameter_space,
                 scoring = 'accuracy', n_jobs = -1, cv = 5)
gs.fit(X_train, y_train)
print("最佳参数为：",gs.best_params_)
print("最佳得分为：",gs.best_score_)


# 再看看它在测试集上的分数：
#   可以看到居然还不如我们之前的参数。这里要注意在进行网格搜索的时候就进行了K折交叉验证的。
#   我一开始是以为网格搜索是在训练集上寻找拟合效果最好的参数，这点需要注意。
model = AdaBoostClassifier(base_estimator=base_model, n_estimators=42, learning_rate = 0.8)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred) # 准确率
print(f"准确率：{acc:.2}")