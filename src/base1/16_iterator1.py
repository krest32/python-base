#!/usr/bin/python3

if __name__ == '__main__':

    list = [1, 2, 3, 4]
    it = iter(list)  # 创建迭代器对象
    for x in it:
        print(x, end=" ")