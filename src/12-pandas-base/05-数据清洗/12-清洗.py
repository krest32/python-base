import pandas as pd

person = {
    "name": ['Google', 'Runoob', 'Taobao'],
    "age": [50, 40, 12345]  # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)
df.loc[2, 'age'] = 30  # 修改数据
print(df.to_string())
