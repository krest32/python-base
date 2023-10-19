import pandas as pd

# 第三个日期格式错误
data = {
    "Date": ['2020/12/01', '2020/12/02', '20201226'],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
