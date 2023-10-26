import keras
import tensorflow as tf
import os

from keras.src.applications.densenet import layers
from keras.src.layers import Dense

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


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

    model.compile(optimizer=..., loss=custom_mean_squared_error)
    model.compile(optimizer=..., loss=CustomMSE())
    


    """
    
    一般来说，损失值 由 损失函数 和 正则化项组成(Objective = Loss + Regularization)。
    
    对于keras模型，正则化项一般在各层中指定，
        例如使用Dense的 kernel_regularizer 和 bias_regularizer 等参数指定权重使用 L1 或者 L2 正则化项，
        此外还可以用kernel_constraint 和 bias_constraint等参数约束权重的取值范围，这也是一种正则化手段。
    
    损失函数在 model.compile 时候指定。
    
        对于回归模型，通常使用的损失函数是平方损失函数 mean_squared_error，简写为 mse，类实现形式为 MeanSquaredError 和 MSE
        对于二分类模型，通常使用的是二元交叉熵损失函数 binary_crossentropy。
        对于多分类模型，如果label是one-hot编码的，则使用交叉熵损失函数 categorical_crossentropy。如果label是序号编码的，则需要使用稀疏类别交叉熵损失函数 sparse_categorical_crossentropy。
        如果有需要，也可以自定义损失函数，自定义损失函数需要接收两个张量y_true，y_pred作为输入参数，并输出一个标量作为损失函数值。
    """
