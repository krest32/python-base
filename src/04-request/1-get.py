#!/usr/bin/python3
# coding=utf-8

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 发送请求
    x = requests.get('https://www.baidu.com/')

    soup = BeautifulSoup(x.content)

    # 返回网页内容
    print(x.content)
