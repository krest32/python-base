import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func_constant1():
    # 0 矩阵， 2行3列
    a = tf.zeros([2, 3], tf.int32)
    print(a)
    # 0 矩阵， 2行2列
    b = tf.ones([2, 2], tf.float32)
    print(b)
    # 8 矩阵， 2行3列
    c = tf.fill([2, 3], 8)
    print(c)


def func_constant2():
    # 10 ~ 13,4个数字
    a = tf.linspace(10.0, 13.0, 4)
    print(a)
    # 3—~18，间隔为3，不包含 18
    b = tf.range(3, 18, 3)
    print(b)


def func_constant3():
    # 定义常量 a
    a = tf.constant(3.0, dtype=tf.float32)
    # 定义常量 b
    b = tf.constant(4.0)  # 也是tf.float32，通过4.0推测出来的类型。
    total = a + b
    print(a)
    print(b)
    print(total)
    c = tf.constant([[1, 2], [3, 4]])
    print(c)


# 等同于 功能 add1
def func_constant4():
    a = tf.add(3, 4)
    print(a)


if __name__ == '__main__':
    func_print_version()
    # func_constant1()
    # func_constant2()
    func_constant3()
    # func_constant4()
