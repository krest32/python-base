# 正则表达式模块
import re

def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}",date) is not None


date1 = "2021-12-03"
date2 = "202-12-03"
date3 = "2021/12-03"
date4 = "2021/12/03"
date5 = "20211203"

print(date1,date_is_right(date1))
print(date2,date_is_right(date2))
print(date3,date_is_right(date3))
print(date4,date_is_right(date4))
print(date5,date_is_right(date5))