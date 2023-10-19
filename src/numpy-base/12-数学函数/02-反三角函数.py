import numpy as np

a = np.array([0, 30, 45, 60, 90])
print('含有正弦值的数组：')
sin = np.sin(a * np.pi / 180)
print(sin)

print('计算角度的反正弦，返回值以弧度为单位：')
inv = np.arcsin(sin)
print(inv)

print('通过转化为角度制来检查结果：')
print(np.degrees(inv))

print('arccos 和 arctan 函数行为类似：')
cos = np.cos(a * np.pi / 180)
print(cos)

print('反余弦：')
inv = np.arccos(cos)
print(inv)

print('角度制单位：')
print(np.degrees(inv))

print('tan 函数：')
tan = np.tan(a * np.pi / 180)
print(tan)

print('反正切：')
inv = np.arctan(tan)
print(inv)

print('角度制单位：')
print(np.degrees(inv))

