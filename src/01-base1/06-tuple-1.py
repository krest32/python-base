#!/usr/bin/python3
# coding=utf-8

if __name__ == '__main__':

    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')

    # 以下修改元组元素操作是非法的。
    # tup1[0] = 100

    # 创建一个新的元组
    tup3 = tup1 + tup2
    print(tup3)