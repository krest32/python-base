import pandas as pd

# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：
# 返回结果其实就是一个 Pandas Series 数据。
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])

# 返回第一列
print(df.iloc[:, [0]])
# 返回第二列
print(df.iloc[:, [1]])
