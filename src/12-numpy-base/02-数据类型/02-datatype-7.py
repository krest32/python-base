import numpy as np

# 下面的示例定义一个结构化数据类型 student，
#  包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

