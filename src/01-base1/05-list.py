#!/usr/bin/python3
from collections import Counter

if __name__ == '__main__':
    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']
    print(list)  # 输出完整列表
    print(list[0])  # 输出列表第一个元素
    print(list[1:3])  # 从第二个开始输出到第三个元素
    print(list[2:])  # 输出从第三个元素开始的所有元素
    print(tinylist * 2)  # 输出两次列表
    print(list + tinylist)  # 连接列表
    list.append("aa")
    print(list)

    # 链表去重
    list1 = [1, 2, 3, 3, 4, 'John', 'Ana', 'Mark', 'John']

    result = []
    [result.append(x) for x in list1 if x not in result]
    print(result)

    # 计算列表中元素的出现频率
    my_list = ['a', 'b', 'b', 'a', 'a', 'a', 'c', 'c', 'b', 'd']
    print(Counter(my_list).most_common())
