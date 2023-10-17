from scipy import stats

if __name__ == '__main__':
    # 预测未来价值
    # 现在，我们可以使用收集到的信息来预测未来的值。
    # 例如：让我们尝试预测一辆拥有 10 年历史的汽车的速度。
    # 为此，我们需要与上例中相同的 myfunc() 函数：

    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    slope, intercept, r, p, std_err = stats.linregress(x, y)


    def myfunc(x):
        return slope * x + intercept


    # 预测一辆有 10年车龄的汽车的速度：
    speed = myfunc(10)

    print(speed)
