import datetime

# 来自日志文件 或者 mysql数据库
time = 1620747224

time_obj = datetime.datetime.fromtimestamp(time)
time_str = time_obj.strftime("%Y-%m-%d")

print(time_str)