import pandas as pd

data = [
    {
        "id": "A001",
        "name": "菜鸟教程",
        "url": "www.runoob.com",
        "likes": 61
    },
    {
        "id": "A002",
        "name": "Google",
        "url": "www.google.com",
        "likes": 124
    },
    {
        "id": "A003",
        "name": "淘宝",
        "url": "www.taobao.com",
        "likes": 45
    }
]
df = pd.DataFrame(data)
print(df)
