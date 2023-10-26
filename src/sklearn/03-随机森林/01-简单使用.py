from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
     clf = RandomForestClassifier(random_state=0)
     X = [[1, 2, 3],  # 2个样本，3个特征
          [11, 12, 13]]
     y = [0, 1]  # 每一个样本的类别

     clf.fit(X, y)
     RandomForestClassifier(random_state=0)

     print(clf.predict(X))
     print(clf.predict([[4, 5, 6], [14, 15, 16]]))
