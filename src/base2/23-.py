import datetime


def getYesterDay():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


if __name__ == '__main__':
    # 输出
    print(getYesterDay())
