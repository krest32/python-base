import datetime

cur_datetime = datetime.datetime.now()

# 获取当前的日期
print(cur_datetime, type(cur_datetime))

# 转化为string
str_time = cur_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)

print("year", cur_datetime.year)
print("month", cur_datetime.month)
print("day", cur_datetime.day)
print("hour", cur_datetime.hour)
print("minute", cur_datetime.minute)
print("second", cur_datetime.second)
