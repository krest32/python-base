import tensorflow as tf
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func_trans():
    a = np.array([
        [1, 2],
        [3, 4]
    ])

    b = tf.convert_to_tensor(a)
    print(b)

    # 第1种 tensor -> numpy
    c = b.numpy()
    print(c)

    # 第2种 tensor -> numpy
    d = np.array(b)
    print(d)


def func_calcul1():
    a = tf.constant([
        [1, 2],
        [3, 4]
    ])
    b = tf.constant([
        [5, 6],
        [7, 8]
    ])

    c = tf.add(a, b)  # 加法 a+b
    print(c)
    d = tf.multiply(a, b)  # 逐元素乘法a * b =
    # [a11 * b11, a12 * b12]
    # [a21 * b21, a22 * b22]

    print(d)
    e = tf.matmul(a, b)  # 矩阵乘法a@b
    print(e)


if __name__ == '__main__':
    func_print_version()
    func_trans()
    func_calcul1()
