import keras
import tensorflow as tf
import os

from keras.src.applications.densenet import layers
from keras.src.layers import Dense
from keras.src.saving.legacy.saved_model.load import metrics

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 自定义度量函数
"""
　继承 tf.keras.metrics.Metric，并且实现4个类方法：
    __init__(self)：创建状态变量
    update_state(self, y_true, y_pred, sample_weight=None)：根据 y_true 和 y_pred 来更新状态变量
    result(self)：使用状态变量来计算 最终结果
    reset_state(self)：重新初始化状态变量
"""
class SnrCustomMetrics(metrics.Metric):
    def __init__(self, name="snr_metrics", **kwargs):
        # 创建状态变量
        super(SnrCustomMetrics, self).__init__(name=name, **kwargs)
        self.metrics_value = self.add_weight(name="snr_value", initializer="zeros")

    def update_state(self, y_true, y_pred, sample_weight=None):
        """使用目标 y_true 和模型预测 y_pred 来更新状态变量
        :param y_true: target
        :param y_pred: 预测值
        :param sample_weight: 权重
        """
        labels_pow = tf.pow(y_true, 2)
        noise_pow = tf.pow(y_pred - y_true, 2)
        snr_value = 10 * tf.math.log(tf.reduce_sum(labels_pow) / tf.reduce_sum(noise_pow)) / tf.math.log(10.)

        if sample_weight is not None:
            sample_weight = tf.cast(sample_weight, "float32")
            snr_value = tf.multiply(snr_value, sample_weight)
        self.metrics_value.assign_add(snr_value)

    # 使用状态变量来计算最终结果
    def result(self):
        return self.metrics_value

    # metrics 的状态将在每个epoch开始时重置。
    def reset_state(self):
        self.metrics_value.assign(0.0)


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


# 自定义损失函数
def custom_mean_squared_error(y_true, y_pred):
    return tf.math.reduce_mean(tf.square(y_true - y_pred))


# 类实现损失函数
class CustomMSE(keras.losses.Loss):
    def __init__(self, regularization_factor=0.1, name="custom_mse"):
        super().__init__(name=name)
        self.regularization_factor = regularization_factor

    def call(self, y_true, y_pred):
        mse = tf.math.reduce_mean(tf.square(y_true - y_pred))
        reg = tf.math.reduce_mean(tf.square(0.5 - y_pred))
        return mse + reg * self.regularization_factor


if __name__ == '__main__':
    func_print_version()

    model = keras.Sequential([
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ])

    model.compile(optimizer=..., loss=..., metrics=[SnrCustomMetrics()])
    model.compile(optimizer=..., loss=CustomMSE())

    """
    人们通常会通过度量函数来从另一个方面 评估模型的好坏，可以在 model.compile 时，通过列表形式指定单/多个评估指标。
    
    model.compile 时，可以
        也可以自定义评估指标。自定义评估指标需要接收两个张量y_true，y_pred作为输入参数，并输出一个标量作为评估值。
        也可以继承 tf.keras.metrics.Metric 自定义度量方法，update_state方法，result方法实现评估指标的计算逻辑，从而得到评估指标的类的实现形式。
    
    """
