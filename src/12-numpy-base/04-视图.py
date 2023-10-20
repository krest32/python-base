import numpy as np

if __name__ == '__main__':
    # 视图不拥有数据，对视图所做的任何更改都会影响原始数组，
    # 而对原始数组所做的任何更改都会影响视图。
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    x[0] = 31

    print(arr)
    print(x)
