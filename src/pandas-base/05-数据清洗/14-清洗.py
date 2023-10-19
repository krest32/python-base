import pandas as pd

person = {
    "name": ['Google', 'Runoob', 'Taobao'],
    "age": [50, 40, 12345]  # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

for x in df.index:
    if df.loc[x, "age"] > 120:
        df.drop(x, inplace=True)

print(df.to_string())
