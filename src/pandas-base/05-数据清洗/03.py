import pandas as pd

df = pd.read_csv('property-data.csv')
new_df = df.dropna()
print(new_df.to_string())