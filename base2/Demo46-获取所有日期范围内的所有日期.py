import datetime

def get_date_range(begin_date,end_date):
    date_List = []
    while begin_date<=end_date:
        date_List.append(begin_date)
        begin_date_obj = datetime.datetime.strptime(begin_date,"%Y-%m-%d")
        days = datetime.timedelta(days=1)
        begin_date = (begin_date_obj+days).strftime("%Y-%m-%d")
    return date_List

begin_date= "2021-04-05"
end_date = "2021-05-05"

date_list = get_date_range(begin_date,end_date)
print(date_list)
