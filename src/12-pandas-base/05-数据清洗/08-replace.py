# 使用 mean() 方法计算列的均值并替换空单元格：
import pandas as pd

df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mean()
df["ST_NUM"].fillna(x, inplace=True)
print(df.to_string())
