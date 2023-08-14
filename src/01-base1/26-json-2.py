#!/usr/bin/python3
# coding=utf-8

import json

if __name__ == '__main__':
    # Python 字典类型转换为 JSON 对象
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data)
    # 写入 JSON 数据
    with open('26-data.json', 'w') as f:
        json.dump(data, f)

    # 读取数据
    with open('26-data.json', 'r') as f:
        data2 = json.load(f)
        print(data2)