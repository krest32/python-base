import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models, layers

# 训练数据
dftrain_raw = pd.read_csv('./data/titanic/train.csv')
# 测试数据
dftest_raw = pd.read_csv('./data/titanic/test.csv')
# 打印前10行数据
print(dftrain_raw.head(10))

#
ax = dftrain_raw['Survived'].value_counts().plot(kind='bar', figsize=(12, 8), fontsize=15, rot=0)
ax.set_ylabel('Counts', fontsize=15)
ax.set_xlabel('Survived', fontsize=15)
plt.show()

ax = dftrain_raw['Age'].plot(kind='hist', bins=20, color='purple', figsize=(12, 8), fontsize=15)

ax.set_ylabel('Frequency', fontsize=15)
ax.set_xlabel('Age', fontsize=15)
plt.show()
