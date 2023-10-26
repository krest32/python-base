import keras
import tensorflow as tf
import os

from keras.src.applications.densenet import layers

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 忽略警告
def func_print_version():
    print("tensorflow-base version: ", tf.__version__)


def create_model1():
    # 顺序建模
    model = keras.Sequential([
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ])


def create_model2():
    model = keras.Sequential()
    # 在第一层添加Input
    model.add(keras.Input(shape=(4,)))
    model.add(layers.Dense(2, activation="relu"))

    # 或者在第一层添加input_shape
    model.add(layers.Dense(2, activation="relu", input_shape=(4,)))


# 函数式 API 搭建模型比 Sequential 更加灵活，可以处理具有非线性拓扑、共享层甚至多个输入或输出的模型。
def create_model3():
    inputs = keras.Input(shape=(784,))
    x = layers.Dense(64, activation="relu")(inputs)
    x = layers.Dense(64, activation="relu")(x)
    outputs = layers.Dense(10)(x)
    model = keras.Model(inputs=inputs, outputs=outputs, name="mnist_model")
    model.summary()  # 查看模型摘要
    keras.utils.plot_model(model, "my_first_model_with_shape_info.png", show_shapes=True)

if __name__ == '__main__':
    func_print_version()
    create_model3()
    """
    深度学习模型一般由各种模型层组合而成，如果这些内置模型层不能够满足需求，我们也可以通过编写tf.keras.Lambda匿名模型层或继承tf.keras.layers.Layer基类构建自定义的模型层。
    其中tf.keras.Lambda匿名模型层只适用于构造没有学习参数的模型层。
        
    搭建模型有以下3种方式构建模型：    
        Sequential顺序模型：用于简单的层堆栈， 其中每一层恰好有一个输入张量和一个输出张量
        函数式API模型：多输入多输出，或者模型需要共享权重，或者模型具有残差连接等非顺序结构，
        继承Model基类自定义模型：如果无特定必要，尽可能避免使用Model子类化的方式构建模型，这种方式提供了极大的灵活性，但也有更大的概率出错
    """
