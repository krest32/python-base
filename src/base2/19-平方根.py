if __name__ == '__main__':
    num = float(input('请输入一个数字： '))
    # ** 获取平方和，0.5获取平方根
    num_sqrt = num ** 0.5
    # %f 取值浮点数，.3，取3位有效小数
    print(' %0.3f 的平方根为 %0.3f' % (num, num_sqrt))
