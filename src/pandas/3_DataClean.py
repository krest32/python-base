import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                       "date": pd.date_range('20130102', periods=6),
                       "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                       "age": [23, 44, 54, 32, 34, 32],
                       "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                       "price": [1200, np.nan, 2133, np.NAN, np.nan, 4432]},
                      columns=['id', 'date', 'city', 'category', 'age', 'price'])

    # 用数字0填充空值：
    df.fillna(value=0)
    print(df.values)

    # 使用列prince的均值对NA进行填充：
    df['price'].fillna(df['price'].mean())
    print(df.values)

    # 清除city字段的字符空格：
    df['city'] = df['city'].map(str.strip)

    # 大小写转换：
    df['city'] = df['city'].str.lower()
    # 更改数据格式：
    df['price'].astype('int')

    # 更改列名称：
    df.rename(columns={'category': 'category-size'})

    # 删除后出现的重复值：
    df['city'].drop_duplicates()

    # 删除先出现的重复值：
    df['city'].drop_duplicates(keep='last')

    # 数据替换：
    df['city'].replace('sh', 'shanghai')
