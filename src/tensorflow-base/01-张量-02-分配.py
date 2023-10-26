import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


if __name__ == '__main__':
    func_print_version()
    # 为了提高性能，TensorFlow 会尝试将张量和变量放在与其 dtype 兼容的最快设备上。
    # 这意味着如果有 GPU，那么大部分变量都会放置在 GPU 上，不过，我们可以重写变量的位置。
    with tf.device('CPU:0'):
        # Create some tensors
        a = tf.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        c = tf.matmul(a, b)

    print(c)
