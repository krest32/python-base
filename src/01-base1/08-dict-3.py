#!/usr/bin/python3
# coding=utf-8

# 合并两个字典
# Python3.5之后，合并字典变得容易起来。我们可以通过**符号解压字典，并将多个字典传入{}中，实现合并。
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# 两个列表转化为字典
def list_to_dictionary(keys, values):
    return dict(zip(keys, values))


if __name__ == '__main__':
    indict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

    print("indict['Age']: ", indict['Age'])
    # print("indict['School']: ", indict['School'])

    del indict['Name']  # 删除键 'Name'
    # indict.clear()  # 清空字典
    del indict  # 删除字典

    # print("indict['Age']: ", indict['Age'])
    # print("indict['School']: ", indict['School'])

    # 合并两个字典
    dict1 = {"name": "Joy", "age": 25}
    dict2 = {"name": "Joy", "city": "New York"}
    dict3 = Merge(dict1, dict2)
    print(dict3)

    # 合并两个字典
    x = {'a': 1, 'b': 2}
    y = {'c': 3, 'd': 4}
    x.update(y)
    print(x)

    # 将两个列表转换为字典
    list1 = [1, 2, 3]
    list2 = ['one', 'two', 'three']
    print(list_to_dictionary(list1, list2))

    # 将字典当中的键值对位置调换
    staff = {'Data Scientist': 'Mike', 'Django Developer': 'Dylan'}
    staff = {i: j for j, i in staff.items()}
    print(staff)
