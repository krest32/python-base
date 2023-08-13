# 字符串长度
def findLen(str):
    count = 0
    while str[count:]:
        count += 1
    return count


if __name__ == '__main__':
    str = "com"
    print(findLen(str))
