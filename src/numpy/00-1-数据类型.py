import numpy as np
if __name__ == '__main__':
    # 使用标量类型
    dt1 = np.dtype(np.int32)
    print(dt1)

    # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
    dt2 = np.dtype('i4')
    print(dt2)

    # 字节顺序标注
    dt3 = np.dtype('<i4')
    print(dt3)

    # 将数据类型应用于 ndarray 对象
    dt4 = np.dtype([('age', np.int8)])
    a1 = np.array([(10,), (20,), (30,)], dtype=dt4)
    print(a1)