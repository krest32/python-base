import statistics
import numpy

if __name__ == '__main__':
    # 平均值
    speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    x = numpy.mean(speed)
    print(x)

    # 排序后，找到中间值
    x = numpy.median(speed)
    print(x)


    # 众数：出现次数最多的数字
    x = statistics.mode(speed)
    print(x)


    