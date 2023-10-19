import pandas as pd

df = pd.read_json('nested_list.json')
print(df.to_string())