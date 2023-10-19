import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 手动创建数据
    df = pd.DataFrame(
        {
            "id": [1001, 1002, 1003, 1004, 1005, 1006],
            "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
            "age": [10, 44, 54, 32, 34, 32],
            "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
            "price": [1200, np.nan, 2133, 5433, np.nan, 4432]
        },
        columns=['id', 'date', 'city', 'category', 'age', 'price']
    )

    # 1、简单的数据采样
    print(df.sample(n=3))
    print("--------------------------------")

    # 2、手动设置采样权重
    weights = [0, 0, 0, 0, 0.5, 0.5]
    print(df.sample(n=2, weights=weights))
    print("--------------------------------")

    # 3、采样后不放回
    print(df.sample(n=6, replace=False))
    print("--------------------------------")

    # 4、采样后放回
    print(df.sample(n=6, replace=True))
    print("--------------------------------")

    # 5、 数据表描述性统计
    # round函数设置显示小数位，T表示转置
    print(df.describe().round(2).T)
    print("--------------------------------")

    # 6、计算列的标准差
    print(df['price'].std())
    print("--------------------------------")
    # 7、计算两个字段间的协方差
    print(df['price'].cov(df['age']))
