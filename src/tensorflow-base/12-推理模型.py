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

    x_test = np.zeros(2)
    y_test = np.zeros(2)

    model = keras.Sequential([
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ])

    model.fit(
        x=None, y=None, batch_size=None, epochs=1, verbose='auto',
        callbacks=None, validation_split=0.0, validation_data=None, shuffle=True,
        initial_epoch=0, steps_per_epoch=None)



    # 推理模型：可以使用以下方法:
    model.predict(x_test)
    model(x_test)
    model.call(x_test)
    model.predict_on_batch(x_test)


    # 推荐优先使用model.predict(ds_test)
    # 方法，既可以对Dataset，也可以对Tensor使用。