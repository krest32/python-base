import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)
# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)
# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

# 显示图表
plt.show()
