#!/usr/bin/python3
# coding=utf-8

import requests

if __name__ == '__main__':
    # 发送请求
    x = requests.get('https://www.runoob.com/')

    # 返回网页内容
    print(x.text)
