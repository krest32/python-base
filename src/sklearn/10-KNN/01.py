from sklearn.datasets import load_digits
import pandas as pd

digits = load_digits()
data = digits.data  # 特征集
target = digits.target  # 目标集
data_pd = pd.DataFrame(data)
print(data_pd)


from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(
    data, target, test_size=0.25, random_state=33)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(train_x, train_y)
predict_y = knn.predict(test_x)
from sklearn.metrics import accuracy_score
score = accuracy_score(test_y, predict_y)
print(score)

