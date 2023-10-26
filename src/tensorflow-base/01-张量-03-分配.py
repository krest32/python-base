import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func_assign():
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])  # (2,2)
    b = tf.constant([[5.0, 6.0], [7.0, 8.0]])  # (2,2)

    # 两个张量链接拼接在一起
    c = tf.concat([a, b], axis=0)  # (4, 2)
    print(c)

    # 两个张量堆叠在一起，会增加维度
    d = tf.stack([a, b], axis=0)  # (2, 2, 2)
    print(d)

    # 拆分张量
    e = tf.split(d, 2, axis=0)  # [(1, 2, 2),(1, 2, 2)]
    print(e)


if __name__ == '__main__':
    func_print_version()
    func_assign()
