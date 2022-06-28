#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456"  # 数据库密码
)

print(mydb)

mycursor = mydb.cursor()

# 打印有哪些数据库
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)