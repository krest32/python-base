import numpy as np

nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print('调用 lexsort() 函数：')
print(ind)

print('使用这个索引来获取排序后的数据：')
print([nm[i] + ", " + dv[i] for i in ind])