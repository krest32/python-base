import time

import keras
import numpy as np
import tensorflow as tf
import os

from keras.src.applications.densenet import layers
from keras.src.layers import Dense
from keras.src.saving.legacy.saved_model.load import metrics

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


if __name__ == '__main__':
    func_print_version()

    model = keras.Sequential([
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ])

    model.fit(
        x=None, y=None, batch_size=None, epochs=1, verbose='auto',
        callbacks=None, validation_split=0.0, validation_data=None, shuffle=True,
        initial_epoch=0, steps_per_epoch=None)

    # 　可以使用Keras方式保存模型，也可以使用TensorFlow原生方式保存。
    #       前者仅仅适合使用Python环境恢复模型，
    #       后者则可以跨平台进行模型部署。推荐使用后一种方式进行保存。

    # -----------------------------方式一--------------------------------------------
    # 保存
    SaveModel_path = 'path/to/location'
    model.save(SaveModel_path)
    # 或者
    tf.keras.models.save_model(model, SaveModel_path)

    # 加载
    model = tf.keras.models.load_model(SaveModel_path)  # 加载模型

    # -----------------------------方式二--------------------------------------------
    # TensorFlow原生方式保存和加载
    # 保存模型结构与模型参数到文件，该方式保存的模型具有跨平台性便于部署
    model.save(..., save_format="tf")  # 保存模型
    model_loaded = tf.keras.models.load_model(...)  # 加载模型
