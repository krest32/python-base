import pandas as pd

# 也可以使用 key/value 对象，类似字典来创建 Series：
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)