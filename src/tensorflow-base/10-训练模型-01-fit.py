import keras
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

    """
    参数：
        
        1. x：输入数据，可以是：
                numpy数组、数组列表(如果模型有多个输入)
                Tensorflow张量或张量列表(如果模型有多个输入)
                如果模型具有命名输入，则将输入名称映射到相应的数组/张量的字典。
                tf.data数据集，应该返回一个(inputs, targets)或 的元组(inputs, targets, sample_weights)
                生成器或keras.utils.Sequence返回(inputs, targets) 或(inputs, targets, sample_weights)。
        2. y：目标数据。与输入数据一样x，它可以是 Numpy 数组或 TensorFlow 张量。它应该是一致的x(你不能有 Numpy 输入和张量目标，或者相反)。如果x是数据集、生成器或keras.utils.Sequence实例，y则不应指定(因为目标将从 获取x)。
        3. batch_size：每次梯度更新的样本数。如果未指定，将默认为 32。如果您的数据是数据集、生成器或实例的形式(因为它们生成批次)，请不要指定。
        4. epochs：训练模型的周期数
        5. verbose：'auto'、0、1 或 2。详细模式。0 =静默，1 = 进度条，2 = 每个 epoch 一行。'auto' 在大多数情况下默认为 1
        6. callbacks：训练期间调用的回调列表。见tf.keras.callbacks。
        7. validation_split：在 0 和 1 之间浮动。从训练数据集中分离一部分数据用于验证，并将在每个 epoch 结束时评估该数据的损失和指标
        8. validation_data：验证数据集
        9. shuffle：布尔值(是否在每个 epoch 之前对训练数据进行洗牌)
        10 initial_epoch：整数。开始训练的epoch(对于恢复之前的训练运行很有用)。
        
        返回：history，调用 history.history 可以查看训练期间损失值和度量值的记录
    """

    """
    train_on_batch
    　　该内置方法相比较fit方法更加灵活，可以不通过回调函数而直接在batch层次上更加精细地控制训练的过程。
    """

    """
        for epoch in tf.range(1, epoches + 1):
        for x, y in ds_train:
            train_result = model.train_on_batch(x, y)

        for x, y in ds_valid:
            valid_result = model.test_on_batch(x, y, reset_metrics=False)
    """

