import timeit
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


# 二阶偏导
def func_gradient1():
    x = tf.Variable(0.0, name="x", dtype=tf.float32)
    a = tf.constant(1.0)
    b = tf.constant(-2.0)
    c = tf.constant(1.0)

    with tf.GradientTape() as tape2:
        with tf.GradientTape() as tape1:
            y = a * tf.pow(x, 2) + b * x + c
        dy_dx = tape1.gradient(y, x)
    dy2_dx2 = tape2.gradient(dy_dx, x)

    print(dy2_dx2)  # tf.Tensor(2.0, shape=(), dtype=float32)


if __name__ == '__main__':
    func_print_version()
    func_gradient1()
