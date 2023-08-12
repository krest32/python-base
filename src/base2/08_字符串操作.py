# 字符串长度
def findLen(str):
    count = 0
    while str[count:] :
        count +=1
    return count

str = "com"
print(findLen(str))