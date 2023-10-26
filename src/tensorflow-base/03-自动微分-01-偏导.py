import timeit
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def func_gradient1():
    x = tf.Variable(0.0, name="x", dtype=tf.float32)
    a = tf.constant(1.0)
    b = tf.constant(-2.0)
    c = tf.constant(1.0)

    # 记录一个计算的公示
    with tf.GradientTape() as tape:
        y = a * tf.pow(x, 2) + b * x + c

    # 计算偏导
    dy_dx = tape.gradient(y, x)
    print(dy_dx)  # tf.Tensor(-2.0, shape=(), dtype=float32)


def func_gradient2():
    x = tf.Variable(0.0, name="x", dtype=tf.float32)
    a = tf.constant(1.0)
    b = tf.constant(-2.0)
    c = tf.constant(1.0)

    # 对常量张量也可以求导，只不过需要增加watch
    with tf.GradientTape() as tape:
        tape.watch([a, b, c])
        y = a * tf.pow(x, 2) + b * x + c

    dy_dx, dy_da, dy_db, dy_dc = tape.gradient(y, [x, a, b, c])
    print(dy_da)  # tf.Tensor(0.0, shape=(), dtype=float32)
    print(dy_dc)  # tf.Tensor(1.0, shape=(), dtype=float32)


if __name__ == '__main__':
    func_print_version()
    func_gradient1()
    # 对常量求偏导
    func_gradient2()
    """
        自动微分用于训练神经网络的反向传播非常有用，TensorFlow 会记住在前向传递过程中哪些运算以何种顺序发生。
        随后，在后向传递期间，以相反的顺序遍历此运算列表来计算梯度。
        Tensorflow一般使用tf.GradientTape来记录正向运算过程，然后反向传播自动计算梯度值。
    """
