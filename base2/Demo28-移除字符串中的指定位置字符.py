str = "Runoob"
newStr = ""
for i in range(0,len(str)):
    if i!=2:
        newStr = newStr+str[i]

print("结果："+newStr)


def check(str,subStr):
    if(str.find(subStr)==-1):
        print("不存在")
    else:
        print("存在")

str = "www.runoob.com"
subStr = "com"
(check(str,subStr))