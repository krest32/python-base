import datetime
date_sale = {}
# 首行开关
is_first_line = True
with open("./Demo48-text.txt", "r", encoding="utf-8-sig")as fin:
    for line in fin:
        # 如果是首行就跳过
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sale = line.split("\t")
        date_sale[date] = float(sale)

print(date_sale)

def get_diff(date, days):
    cur_date = datetime.datetime.strptime(date, "%Y/%m/%d")
    timedelta = datetime.timedelta(days = -days)
    return (cur_date + timedelta).strftime("%Y/%m/%d")


for date, sale in date_sale.items():
    date7 = get_diff(date, 7)
    # 获取默认的数据
    sale_num7 = date_sale.get(date7, 0)
    if sale_num7 == 0:
        print(date, sale, 0)
    else:
        week_diff = (sale-sale_num7) / sale_num7
        print(date, sale, date7, sale_num7, week_diff)
