import pandas as pd

df = pd.read_csv('nba.csv')
print(df.to_string())
# to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
