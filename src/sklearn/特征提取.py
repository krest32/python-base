from sklearn.feature_extraction import DictVectorizer

v = DictVectorizer(sparse=False)
D = [
    {'foo': 1, 'bar': 2},
    {'foo': 3, 'baz': 1}
]
X = v.fit_transform(D)
print(X)
