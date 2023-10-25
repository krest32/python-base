from sklearn import datasets
from sklearn import svm


def load1():
    iris = datasets.load_iris()
    digits = datasets.load_digits()

    print(iris)
    print(digits)


def load2():
    clf = svm.SVC(gamma=0.001, C=100.)
    digits = datasets.load_digits()
    clf.fit(digits.data[:-1], digits.target[:-1])
    print(clf.predict(digits.data[-1:]))

if __name__ == '__main__':
    load1()
    load2()
