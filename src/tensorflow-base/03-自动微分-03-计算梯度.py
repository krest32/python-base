import timeit
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func_gradient1():
    # 求f(x) = a*x**2 + b*x + c的最小值
    # 使用optimizer.apply_gradients

    x = tf.Variable(0.0, name="x", dtype=tf.float32)
    a = tf.constant(1.0)
    b = tf.constant(-2.0)
    c = tf.constant(1.0)

    optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
    for _ in range(1000):
        with tf.GradientTape() as tape:
            y = a * tf.pow(x, 2) + b * x + c
        dy_dx = tape.gradient(y, x)  # 计算梯度
        optimizer.apply_gradients(grads_and_vars=[(dy_dx, x)])  # 根据梯度更新变量

    tf.print("y =", y, "; x =", x)


if __name__ == '__main__':
    func_print_version()
    func_gradient1()
