#!/usr/bin/python3

if __name__ == '__main__':
    dict = {'one': "1 - 菜鸟教程", 2: "2 - 菜鸟工具"}
    tinyDict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

    print(dict['one'])  # 输出键为 'one' 的值
    print(dict[2])  # 输出键为 2 的值
    print(tinyDict)  # 输出完整的字典
    print(tinyDict.keys())  # 输出所有键
    print(tinyDict.values())  # 输出所有值

    if "haha" in tinyDict:
        print("ok")
