import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_mix.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df)
