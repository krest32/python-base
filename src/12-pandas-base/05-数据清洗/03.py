import pandas as pd

df = pd.read_csv('property-data.csv')
# 丟掉為 null 的列
new_df = df.dropna()
print(new_df.to_string())