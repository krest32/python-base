from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest, chi2

X, y = load_digits(return_X_y=True)
## 特征选择
X_new = SelectKBest(chi2, k=20).fit_transform(X, y)

print(X_new)