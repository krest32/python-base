from numpy import random

if __name__ == '__main__':
    # 100 以内的随机整数
    x = random.randint(100)
    print(x)

    # 随机浮点数
    x = random.rand()
    print(x)

    # 随机数字长度 5， 每个数字小于 100
    x = random.randint(100, size=(5))
    print(x)

    # 生成有 3 行的 2-D 数组，每行包含 5 个从 0 到 100 之间的随机整数：
    x = random.randint(100, size=(3, 5))
    print(x)

    # 生成包含 5 个随机浮点数的 1-D 数组：
    x = random.rand(5)
    print(x)

    # 生成有 3 行的 2-D 数组，每行包含 5 个随机数：
    x = random.rand(3, 5)
    print(x)

    # choice() 方法使您可以基于值数组生成随机值。
    # choice() 方法将数组作为参数，并随机返回其中一个值。
    x = random.choice([3, 5, 7, 9])
    print(x)

    # 生成由数组参数（3、5、7 和 9）中的值组成的二维数组：
    x = random.choice([3, 5, 7, 9], size=(3, 5))
    print(x)
