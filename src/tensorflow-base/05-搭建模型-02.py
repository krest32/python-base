import keras
import tensorflow as tf
import os

from keras.src.applications.densenet import layers
from keras.src.layers import Dense

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class SequentialModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.dense_1 = Dense(in_features=3, out_features=3)
        self.dense_2 = Dense(in_features=3, out_features=2)

    def __call__(self, x):
        x = self.dense_1(x)
        return self.dense_2(x)


my_model = SequentialModule(name="the_model")


# 继承tf.Module栗子：
class ResBlock(layers.Layer):
    def __init__(self, kernel_size, **kwargs):
        super(ResBlock, self).__init__(**kwargs)
        self.kernel_size = kernel_size

    def build(self, input_shape):
        self.conv1 = layers.Conv1D(filters=64, kernel_size=self.kernel_size,
                                   activation="relu", padding="same")
        self.conv2 = layers.Conv1D(filters=32, kernel_size=self.kernel_size,
                                   activation="relu", padding="same")
        self.conv3 = layers.Conv1D(filters=input_shape[-1],
                                   kernel_size=self.kernel_size, activation="relu", padding="same")
        self.maxpool = layers.MaxPool1D(2)
        super(ResBlock, self).build(input_shape)  # 相当于设置self.built = True

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.conv2(x)
        x = self.conv3(x)
        x = layers.Add()([inputs, x])
        x = self.maxpool(x)
        return x

    # 如果要让自定义的Layer通过Functional API 组合成模型时可以序列化，需要自定义get_config方法。
    def get_config(self):
        config = super(ResBlock, self).get_config()
        config.update({'kernel_size': self.kernel_size})
        return config


resblock = ResBlock(kernel_size=3)
resblock.build(input_shape=(None, 200, 7))
resblock.compute_output_shape(input_shape=(None, 200, 7))


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


if __name__ == '__main__':
    func_print_version()
