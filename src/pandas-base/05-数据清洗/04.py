import pandas as pd

# 注意：默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数:
df = pd.read_csv('property-data.csv')
df.dropna(inplace = True)
print(df.to_string())