import numpy as np

if __name__ == '__main__':
    arr = np.array(
        [4, 2]
    )
    print(arr)

    # 此函数为扩展函数，data为要扩展的数据，类型为np类型数组，x,扩展行数，y扩展列数，
    print(np.tile(arr, (6, 1)))
