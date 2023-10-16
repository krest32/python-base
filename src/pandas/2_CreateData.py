import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 手动创建数据
    df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                       "date": pd.date_range('20130102', periods=6),
                       "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                       "age": [23, 44, 54, 32, 34, 32],
                       "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                       "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                      columns=['id', 'date', 'city', 'category', 'age', 'price'])

    # 维度查看：
    print(df.shape)
    # 数据表基本信息（维度、列名称、数据格式、所占空间等）
    print(df.info)
    # 每一列数据的格式：
    print(df.dtypes)
    # 空值
    print(df.isnull)
    # 查看某一列的唯一值：
    print(df['id'].unique())
    # 查看数据表的值：
    print(df.values)
    # 查看列名称：
    print(df.columns)
    # 查看前5行数据、后5行数据：
    print("--------------------")
    df.head()  # 默认前5行数据
    df.tail()  # 默认后5行数据
