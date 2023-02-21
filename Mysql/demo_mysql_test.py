# !/usr/bin/python3

import pymysql
# 需要 8.0 需要安装插件： python -m  pip install cryptography  -i https://pypi.tuna.tsinghua.edu.cn/simple
# python连接数据库报错“：RuntimeError: ‘cryptography’ package is required for sha256_password or caching_sha2_password auth methods
# 该错误提示的意思是：sha256_password和caching_sha2_password两种加密方式需要cryptography。

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='demo')



# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)
