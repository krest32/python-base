import pandas as pd

# 索引值就从 0 开始，我们可以根据索引值读取数据：
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar[1])