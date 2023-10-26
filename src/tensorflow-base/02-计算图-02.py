import timeit
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


@tf.function  # 在TensorFlow2.0中使用静态图
def str_join(x, y):
    z = tf.strings.join([x, y], separator=" ")
    tf.print(z)
    return z


def power(x, y):
    result = tf.eye(10, dtype=tf.dtypes.int32)
    for _ in range(y):
        result = tf.matmul(x, result)
    return result


if __name__ == '__main__':
    func_print_version()
    # 测量静态图 和 动态图性能差异

    # 静态图
    x = tf.random.uniform(shape=[10, 10], minval=-1, maxval=2, dtype=tf.dtypes.int32)
    print("Eager execution:", timeit.timeit(lambda: power(x, 100), number=1000))  # 2.56378621799

    # 动态图
    # 将 python 函数转换为图形
    power_as_graph = tf.function(power)
    print("Graph execution:", timeit.timeit(lambda: power_as_graph(x, 100), number=1000))  # 0.683253670

    """
        有三种计算图的构建方式：静态计算图，动态计算图，以及Autograph。
            在TensorFlow1.0时代，采用的是静态计算图，需要先使用TensorFlow的各种算子创建计算图，然后再开启一个会话Session，显式执行计算图。
            而在TensorFlow2.0时代，采用的是动态计算图，即每使用一个算子后，该算子会被动态加入到隐含的默认计算图中立即执行得到结果，而无需开启Session。
                使用动态计算图(Eager Excution)的好处是方便调试程序，它会让TensorFlow代码的表现和Python原生代码的表现一样，写起来就像写numpy一样，各种日志打印，控制流全部都是可以使用的。
                使用动态计算图的缺点是运行效率相对会低一些。
                    因为使用动态图会有许多次Python进程和TensorFlow的C++进程之间的通信。
                而静态计算图构建完成之后几乎全部在TensorFlow内核上使用C++代码执行，效率更高。
                此外静态图会对计算步骤进行一定的优化，剪去和结果无关的计算步骤。   
    　　 如果需要在TensorFlow2.0中使用静态图，可以使用@tf.function装饰器将普通Python函数转换成对应的TensorFlow计算图构建代码。
        运行该函数就相当于在TensorFlow1.0中用Session执行代码。
        使用tf.function构建静态图的方式叫做 Autograph。
        当然Autograph机制能够转换的代码并不是没有任何约束的，有一些编码规范需要遵循，否则可能会转换失败或者不符合预期。
    """