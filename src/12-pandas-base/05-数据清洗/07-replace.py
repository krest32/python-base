import pandas as pd

# 用 12345 替换 PID 为空数据：
df = pd.read_csv('property-data.csv')
df['PID'].fillna(12345, inplace = True)
print(df.to_string())