# DataFrame 构造方法如下：
# pandas.DataFrame( data, index, columns, dtype, copy)
# 参数说明：
#    data：一组数据(ndarray、series, map, lists, dict 等类型)。
#    index：索引值，或者可以称为行标签。
#    columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
#    dtype：数据类型
#    copy：拷贝数据，默认为 False。

import pandas as pd

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=float)
print(df)
