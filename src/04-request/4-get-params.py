#!/usr/bin/python3
# coding=utf-8

import requests

if __name__ == '__main__':
    # 表单参数
    kw = {'s': 'python 教程'}
    cookies = {"key": "value"}
    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }

    # params 接收 字典 或者 字符串 的查询参数，字典类型自动转换为 url 编码，不需要 url encode()
    response = requests.get("https://www.runoob.com/", params=kw, headers=headers, cookies=cookies)

    # 查看响应状态码
    print(response.status_code)
    # 查看响应头部字符编码
    print(response.encoding)
    # 查看完整url地址
    print(response.url)
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)
