import tensorflow as tf
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


@tf.function  # 在TensorFlow2.0中使用静态图
def str_join(x, y):
    z = tf.strings.join([x, y], separator=" ")
    tf.print(z)
    return z


if __name__ == '__main__':
    func_print_version()
    result = str_join(tf.constant("hello"), tf.constant("world"))
    print(result)
