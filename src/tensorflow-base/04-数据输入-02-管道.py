import random
import string
import numpy as np
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


if __name__ == '__main__':
    func_print_version()
    """
    训练深度学习模型常常会非常耗时。模型训练的耗时主要来自于两个部分，一部分来自数据准备，另一部分来自参数迭代。参数迭代过程的耗时通常依赖于GPU来提升。
    而数据准备过程的耗时则可以通过构建高效的数据管道进行提升。
    以下是一些构建高效数据管道的建议。
        
        使用 prefetch 方法让数据准备和参数迭代两个过程相互并行。
        使用 interleave 方法可以让数据读取过程多进程执行，并将不同来源数据夹在一起。
        使用 map 时设置num_parallel_calls 让数据转换过程多进行执行。
        使用 cache 方法让数据在第一个epoch后缓存到内存中，仅限于数据集不大情形。
        使用 map转换时，先batch，然后采用向量化的转换方法对每个batch进行转换。
    """
