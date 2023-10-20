import pandas as pd
import json

# 这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来：
# 使用 Python JSON 模块载入数据
with open('nested_list.json', 'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path=['students'])
print(df_nested_list)
