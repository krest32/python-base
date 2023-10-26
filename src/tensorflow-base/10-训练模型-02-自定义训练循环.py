import time

import keras
import tensorflow as tf
import os

from keras.src.applications.densenet import layers
from keras.src.layers import Dense
from keras.src.saving.legacy.saved_model.load import metrics

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


optimizer = keras.optimizers.SGD(learning_rate=1e-3)  # 实例化一个优化器
loss_fn = keras.losses.BinaryCrossentropy()  # 实例化损失函数

train_loss = keras.metrics.Mean(name='train_loss')
valid_loss = keras.metrics.Mean(name='valid_loss')

train_metric = keras.metrics.BinaryAccuracy(name='train_accuracy')
valid_metric = keras.metrics.BinaryAccuracy(name='valid_accuracy')


@tf.function
def train_step(features, labels):
    with tf.GradientTape() as tape:
        logits = model(features, training=True)
        loss_value = loss_fn(labels, logits)
        # loss_value += sum(model.losses)   # 添加额外的损失
    grads = tape.gradient(loss_value, model.trainable_weights)
    optimizer.apply_gradients(zip(grads, model.trainable_weights))

    train_loss.update_state(loss_value)
    train_metric.update_state(labels, logits)


@tf.function
def valid_step(features, labels):
    val_logits = model(features, training=False)

    loss_value = loss_fn(labels, val_logits)
    valid_loss.update_state(loss_value)
    valid_metric.update_state(labels, val_logits)


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

    epochs = 2
    for epoch in range(epochs):
        start_time = time.time()
        for step, (x_batch_train, y_batch_train) in enumerate(train_dataset):
            loss_value = train_step(x_batch_train, y_batch_train)
        # 在每个epoch结束时运行验证循环
        for x_batch_val, y_batch_val in val_dataset:
            valid_step(x_batch_val, y_batch_val)

        if epoch % 5 == 0:
            print('Epoch={},Loss:{},Accuracy:{},Valid Loss:{},Valid Accuracy:{}'.format(epoch, train_loss.result(),
                                                                                        train_metric.result(),
                                                                                        valid_loss.result(),
                                                                                        valid_metric.result()))
        train_loss.reset_states()
        valid_loss.reset_states()
        train_metric.reset_states()
        valid_metric.reset_states()

        print("运行时间: %.2fs" % (time.time() - start_time))

        """
        自定义训练循环：自定义训练循环无需编译模型，直接利用优化器根据损失函数反向传播迭代参数，拥有最高的灵活性。
        
        训练循环包括按顺序重复执行三个任务：
            给模型输入batch数据以生成输出
            通过将输出与标签进行比较来计算损失
            使用GradientTape计算梯度
            使用这些梯度优化变量
        """