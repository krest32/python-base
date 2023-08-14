
if __name__ == '__main__':
    lst = [10, 20, 30, 41]

    # 排序
    lst.sort()
    print("最小元素：", *lst[:1])

    # 使用min函数
    list1 = [10, 20, 1, 45, 99]
    print("最小元素为:", min(list1))

    list1 = [10, 20, 1, 45, 99]
    print("最大元素为:", max(list1))
