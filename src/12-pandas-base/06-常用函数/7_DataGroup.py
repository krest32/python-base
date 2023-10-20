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

    # 1、对所有的列进行计数汇总
    print(df.groupby('city').count())

    # 2、按城市对id字段进行计数
    print(df.groupby('city')['id'].count())

    # 3、对两个字段进行汇总计数
    df.groupby(['city', 'price'])['id'].count()

    # 4、对city字段进行汇总，并分别计算prince的合计和均值
    print(df.groupby('city')['price'].agg([len, np.sum, np.mean]))
