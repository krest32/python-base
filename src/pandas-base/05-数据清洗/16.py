import pandas as pd

persons = {
    "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
    "age": [50, 40, 40, 23]
}

df = pd.DataFrame(persons)
df.drop_duplicates(inplace=True)
print(df)
