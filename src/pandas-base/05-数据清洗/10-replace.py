import pandas as pd

# 使用 mode() 方法计算列的众数并替换空单元格：
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mode()
df["ST_NUM"].fillna(x, inplace = True)
print(df.to_string())