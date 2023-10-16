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

    # 按索引提取单行的数值
    print(df.loc[3])

    # 按索引提取区域行数值
    print(df.iloc[0:5])

    # 重设索引
    df.reset_index()

    # 设置日期为索引
    df2 = df.set_index('date')

    # 提取4日之前的所有数据
    print(df2[:'2013-01-04'])

    # 使用iloc按位置区域提取数据
    # 冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列。
    print(df.iloc[:3, :2])

    # 7、适应iloc按位置单独提起数据
    # 提取第0、2、5行，4、5列
    print(df.iloc[[0, 2, 5], [4, 5]])

    # 9、判断city列的值是否为北京
    print(df['city'].isin(['beijing']))

    # 10、判断city列里是否包含beijing和shanghai，然后将符合条件的数据提取出来
    print(df.loc[df['city'].isin(['beijing', 'shanghai'])])

    # 11、提取前三个字符，并生成数据表
    df3 = pd.DataFrame(df['category'].str[:3])
    print(df3.values)
