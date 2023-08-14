#!/usr/bin/python3
# coding=utf-8

import requests

if __name__ == '__main__':
    # 发送请求
    x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')

    print(x.text)
    print("-----------------------")
    print(x.content)
    print("-----------------------")
    # 返回 json 数据
    print(x.json())