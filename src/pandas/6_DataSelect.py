import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 手动创建数据
    df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                       "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                       "age": [10, 44, 54, 32, 34, 32],
                       "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                       "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                      columns=['id', 'date', 'city', 'category', 'age', 'price'])

    # 使用与、或、非三个条件配合大于、小于、等于对数据进行筛选，并进行计数和求和。

    # 1、使用“与”进行筛选
    print(df.loc[(df['age'] > 20) & (df['city'] == 'beijing'), ['id', 'city', 'age', 'category', 'price']])
    print("----------------------------")
    # 2、使用“或”进行筛选
    print(df.loc[(df['age'] > 25) | (df['city'] == 'beijing'), ['id', 'city', 'age', 'category', 'price']])
    print("----------------------------")
    # 3、使用“非”条件进行筛选
    print(df.loc[(df['city'] != 'beijing'), ['id', 'city', 'age', 'category', 'price']])
    print("----------------------------")
    # 4、对筛选后的数据按city列进行计数
    print(df.loc[(df['city'] != 'beijing'), ['id', 'city', 'age', 'category', 'price']].city.count())
    print("----------------------------")
    # 5、使用query函数进行筛选
    print(df.query('city == ["beijing", "shanghai"]'))
    print("----------------------------")
    # 6、对筛选后的结果按prince进行求和
    print(df.query('city == ["beijing", "shanghai"]').price.sum())
    print("----------------------------")
