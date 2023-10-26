import numpy as np
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func1():
    features = np.arange(0, 100, dtype=np.int32)  # # (100,) 整数型数字，从1~100，不包含100
    labels = np.zeros(100, dtype=np.int32)  # (100,) 整数型数组填充数字0，长度  100

    data = tf.data.Dataset.from_tensor_slices((features, labels))  # 创建数据集
    data = data.repeat()  # 无限期地补充数据, repeat的功能就是将整个序列重复多次，一般不带参数
    data = data.shuffle(buffer_size=100)  # 打乱数据
    data = data.batch(batch_size=4)  # 构建batch
    data = data.prefetch(buffer_size=1)  # 预取批处理(预加载批处理，消耗更快)

    for batch_x, batch_y in data.take(5):  # 采样，从开始位置取前几个元素
        print(batch_x.shape, batch_y.shape)  # (4,) (4,)
        break


def func2():
    features = np.arange(0, 100, dtype=np.int32)  # # (100,) 整数型数字，从1~100，不包含100
    labels = np.zeros(100, dtype=np.int32)  # (100,) 整数型数组填充数字0，长度  100

    data = tf.data.Dataset.from_tensor_slices((features, labels))  # 创建数据集
    data = data.repeat()  # 无限期地补充数据, repeat的功能就是将整个序列重复多次，一般不带参数
    data = data.shuffle(buffer_size=100)  # 打乱数据
    data = data.batch(batch_size=4)  # 构建batch
    data = data.prefetch(buffer_size=1)  # 预取批处理(预加载批处理，消耗更快)

    # 如果你打算多次调用，你可以使用迭代器的方式：
    ite_data = iter(data)
    for i in range(5):
        batch_x, batch_y = next(ite_data)
        print(batch_x, batch_y)
        break

    for i in range(5):
        batch_x, batch_y = next(ite_data)
        print(batch_x, batch_y)
        break

if __name__ == '__main__':
    func_print_version()
    func1()
    func2()

    """
    官方推荐使用 tf.data.Dataset.from_tensors() 或 tf.data.Dataset.from_tensor_slices() 创建数据集，
    Dataset支持一类特殊的操作Trainformation(打乱、生成epoch...等操作)
    
        data.map(function)：将转换函数映射到数据集每一个元素
        data.batch(batch_size)：构建batch
        data.shuffle(buffer_size)：随机打乱输入数据，从该缓冲区中随机采样元素
        data.repeat()：repeat的功能就是将整个序列重复多次，一般不带参数
        data.prefetch(tf.data.experimental.AUTOTUNE)  ：预先取 数据
        data.take()：采样，从开始位置取前几个元素
    """
