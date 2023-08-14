def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


if __name__ == '__main__':
    a = 1
    print(id(a))
    change(a)
