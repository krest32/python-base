#!/usr/bin/python3

if __name__ == '__main__':
    a, b, c, d = 20, 5.5, True, 4 + 3j
    # 显示数据类型
    print(type(a), type(b), type(c), type(d))

    # 判断是哪种类型
    a = 111
    print(isinstance(a, int))

    # bool 是 int 的子类
    print(issubclass(bool, int))

    print(True == 1)
