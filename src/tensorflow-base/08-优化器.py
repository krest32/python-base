import keras
import tensorflow as tf
import os

from keras import optimizers
from keras.src.applications.densenet import layers
from keras.src.layers import Dense
from keras.src.saving.legacy.saved_model.load import metrics

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 自定义度量函数
"""
机器学习界有一群炼丹师，他们每天的日常是：拿来药材(数据)，架起八卦炉(模型)，点着六味真火(优化算法)，就摇着蒲扇等着丹药出炉了。
不过，当过厨子的都知道，同样的食材，同样的菜谱，但火候不一样了，这出来的口味可是千差万别。
火小了夹生，火大了易糊，火不匀则半生半糊。
机器学习也是一样，模型优化算法的选择直接关系到最终模型的性能。有时候效果不好，未必是特征的问题或者模型设计的问题，很可能就是优化算法的问题。

　　深度学习优化算法大概经历了 SGD -> SGDM -> NAG ->Adagrad -> Adadelta(RMSprop) -> Adam -> Nadam 这样的发展历程。
    model.compile(optimizer=optimizers.SGD(learning_rate=0.01), loss=loss)
    
    SGD：默认参数为纯SGD, 设置momentum参数不为0实际上变成SGDM, 考虑了一阶动量, 设置 nesterov为True后变成NAG，即 Nesterov Acceleration Gradient，在计算梯度时计算的是向前走一步所在位置的梯度
    Adagrad：考虑了二阶动量，对于不同的参数有不同的学习率，即自适应学习率。缺点是学习率单调下降，可能后期学习速率过慢乃至提前停止学习
    RMSprop：考虑了二阶动量，对于不同的参数有不同的学习率，即自适应学习率，对Adagrad进行了优化，通过指数平滑只考虑一定窗口内的二阶动量
    Adadelta：考虑了二阶动量，与RMSprop类似，但是更加复杂一些，自适应性更强
    Adam：同时考虑了一阶动量和二阶动量，可以看成RMSprop上进一步考虑了Momentum
    Nadam：在Adam基础上进一步考虑了 Nesterov Acceleration
    　　对于一般新手炼丹师，优化器直接使用Adam，并使用其默认参数就OK了。
        一些爱写论文的炼丹师由于追求评估指标效果，可能会偏爱前期使用Adam优化器快速下降，后期使用SGD并精调优化器参数得到更好的结果。
            此外目前也有一些前沿的优化算法，据称效果比Adam更好，例如LazyAdam，Look-ahead，RAdam，Ranger等。
    
    　　初始化优化器时会创建一个变量optimier.iterations用于记录迭代的次数。因此优化器和tf.Variable一样，一般在@tf.function外创建。
    优化器主要使用apply_gradients方法传入变量和对应梯度从而来对给定变量进行迭代，
    

"""


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


@tf.function
def train(epoch=1000):
    for _ in tf.range(epoch):
        optimizer.minimize(loss, model.trainable_weights)
    tf.print("epoch = ", optimizer.iterations)
    return loss


def loss(y_true, y_pred):
    return tf.math.reduce_mean(tf.square(y_true - y_pred))


if __name__ == '__main__':
    func_print_version()

    model = keras.Sequential([
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ])

    optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

    with tf.GradientTape() as tape:
        ...
    grads = tape.gradient(loss, model.trainable_weights)  # 根据损失 求梯度
    optimizer.apply_gradients(zip(grads, model.trainable_weights))  # 根据梯度 优化模型
    model.compile(optimizer=optimizers.SGD(learning_rate=0.01), loss=loss)
