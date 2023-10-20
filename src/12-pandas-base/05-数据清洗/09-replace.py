import pandas as pd

# 使用 median() 方法计算列的中位数并替换空单元格：
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].median()
df["ST_NUM"].fillna(x, inplace = True)
print(df.to_string())