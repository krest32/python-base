import datetime

def get_diff(pdate,days):
    pdate_obj = datetime.datetime.strptime(pdate,"%Y-%m-%d")
    time_gap= datetime.timedelta(days = days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime("%Y-%m-%d")

print(get_diff("2021-04-28", 1))
print(get_diff("2021-04-28", 2))
print(get_diff("2021-04-28", 3))
print(get_diff("2021-04-01", 3))