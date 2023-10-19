import pandas as pd

person = {
    "name": ['Google', 'Runoob', 'Taobao'],
    "age": [50, 200, 12345]
}

df = pd.DataFrame(person)

for x in df.index:
    if df.loc[x, "age"] > 120:
        df.loc[x, "age"] = 120
print(df.to_string())
