import pandas as pd

# 移除 ST_NUM 列中字段值为空的行：
df = pd.read_csv('property-data.csv')
df.dropna(subset=['ST_NUM'], inplace = True)
print(df.to_string())