#!/usr/bin/python3
# coding=utf-8

import json

if __name__ == '__main__':
    # -*- coding: utf-8 -*-
    odata = {'a': '你好'}
    # 乱码
    # json.dumps 序列化时对中文默认使用的ascii编码，
    # print json.dumps(odata)输出unicode编码的结果
    print(json.dumps(odata))

    # 不使用的ascii编码，以gbk编码
    print(json.dumps(odata, ensure_ascii=False))
