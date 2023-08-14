#!/usr/bin/python3
# coding=utf-8

if __name__ == '__main__':
    indict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

    print("indict['Age']: ", indict['Age'])
    print("indict['School']: ", indict['School'])

    del indict['Name']  # 删除键 'Name'
    indict.clear()  # 清空字典
    del indict  # 删除字典

    print("indict['Age']: ", indict['Age'])
    print("indict['School']: ", indict['School'])
