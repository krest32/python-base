import numpy as np

if __name__ == '__main__':

    arr = np.array([61, 62, 63, 64, 65])
    # 创建一个空列表
    filter_arr = []
    # 遍历 arr 中的每个元素
    for element in arr:
        # 如果元素大于 62，则将值设置为 True，否则为 False：
        if element > 62:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)
