#!/usr/bin/python3
# coding=utf-8

import requests

if __name__ == '__main__':
    # 表单参数，参数名为 fname 和 lname
    my_obj = {'fname': 'RUNOOB', 'lname': 'Boy'}
    # 所携带的 cookies
    cookies = {"key": "value"}
    # 发送请求
    x = requests.post('https://www.runoob.com/try/ajax/demo_post2.php', data=my_obj, cookies=cookies)
    # 返回网页内容
    print(x.text)

    """
    headers = {'User-Agent': 'Mozilla/5.0'}  # 设置请求头
    params = {'key1': 'value1', 'key2': 'value2'}  # 设置查询参数
    data = {'username': 'example', 'password': '123456'}  # 设置请求体
    response = requests.post('https://www.runoob.com', headers=headers, params=params, data=data)
    """
