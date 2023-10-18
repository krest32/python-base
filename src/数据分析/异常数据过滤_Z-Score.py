import numpy as np
import pandas as pd


# 如果数据不服从正态分布，则可以用『与平均值的距离是标准差的多少倍』来描述，这个倍数就是 Z-score。
# Z-Score 以标准差（）为单位，去度量某一原始分数（）偏离平均数（ 的距离。
# Z-Score 需要根据经验和实际情况来决定，通常把远离标准差3倍距离以上的数据点视为离群点。
def detect_outliers(data, threshold=3):
    mean_d = np.mean(data)
    std_d = np.std(data)
    outliers = []
    for y in data:
        z_score = (y - mean_d) / std_d
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers
