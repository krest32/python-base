import numpy as np
import pandas as pd

data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=22, header=None)

boston = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :3]]) # 加载数据集
print(type(boston))
print(boston.data.shape)  # （506，13）
print(boston.data.tostring())
