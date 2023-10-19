import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# 指定索引值
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
