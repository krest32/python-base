import datetime

birthday = "1997-12-10"
birthday_date  = datetime.datetime.strptime(birthday,"%Y-%m-%d")
print(birthday_date,type(birthday_date))

cur_datetime = datetime.datetime.now()
print(cur_datetime, type(cur_datetime))

minutes = cur_datetime-birthday_date
print(minutes, type(minutes))

print(minutes.days)