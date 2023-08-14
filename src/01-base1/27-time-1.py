import calendar

if __name__ == '__main__':
    yy = int(input("输入年份："))
    mm = int(input("输入月份："))

    print(calendar.month(yy, mm))
