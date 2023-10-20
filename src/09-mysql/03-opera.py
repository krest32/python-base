# !/usr/bin/python3

import pymysql

# 需要 8.0 需要安装插件： python -m  pip install cryptography  -i https://pypi.tuna.tsinghua.edu.cn/simple
# python连接数据库报错“：RuntimeError: ‘cryptography’ package is required for sha256_password or caching_sha2_password auth methods
# 该错误提示的意思是：sha256_password和caching_sha2_password两种加密方式需要cryptography。

if __name__ == '__main__':
    db = pymysql.connect(host='121.196.111.229',
                         user='root',
                         password='Bob.123456',
                         database='demo')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 异常处理
    try:
        sql = "INSERT INTO sites1 (name, url) VALUES (%s, %s)"
        val = ("RUNOOB", "https://www.runoob.com")
        cursor.execute(sql, val)
        db.commit()
        # 数据表内容有更新，必须使用到该语句
        print(cursor.rowcount, "记录插入成功。")
    except Exception:
        # 执行回滚
        db.rollback()

    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = [
        ('Google', 'https://www.google.com'),
        ('Github', 'https://www.github.com'),
        ('Taobao', 'https://www.taobao.com'),
        ('stackoverflow', 'https://www.stackoverflow.com/')
    ]

    cursor.executemany(sql, val)
    db.commit()  # 数据表内容有更新，必须使用到该语句

    print(cursor.rowcount, "记录插入成功。")

    # 查詢
    result = []
    cursor.execute("SELECT * FROM sites")
    result = cursor.fetchall()  # fetchall() 获取所有记录
    for x in result:
        print(x)

    # 关闭资源
    # 关闭游标对象
    cursor.close()
    # 关闭数据库连接
    db.close()
