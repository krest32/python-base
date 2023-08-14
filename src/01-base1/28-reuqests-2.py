#!/usr/bin/python3
# coding=utf-8

import requests

if __name__ == '__main__':
    # 发送请求
    x = requests.get('https://www.runoob.com/')

    # 返回 http 的状态码
    print(x.status_code)

    # 响应状态的描述
    print(x.reason)

    # 返回编码
    print(x.apparent_encoding)