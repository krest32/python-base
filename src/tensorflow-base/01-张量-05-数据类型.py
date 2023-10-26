import tensorflow as tf
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func_trans():
    a = tf.constant([2.2, 3.3, 4.4], dtype=tf.float64)
    print(a)
    # tensorflow支持的模型有：tf.float16、tf.float64、tf.int8、tf.int16、tf.int32...
    b = tf.cast(a, dtype=tf.float16)  # 类型转换
    print(b)


if __name__ == '__main__':
    func_print_version()
    func_trans()
