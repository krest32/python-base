import pandas as pd

# 使用 12345 替换空字段：
df = pd.read_csv('property-data.csv')
df.fillna(12345, inplace = True)
print(df.to_string())