import pandas as pd
import json

# 使用 Python JSON 模块载入数据
# json_normalize() 使用了参数 record_path 并设置为 ['students'] 用于展开内嵌的 JSON 数据 students。
# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：
with open('nested_list.json', 'r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path=['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)
