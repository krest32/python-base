import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models, layers


# 生存死亡直方图
def survived_png(dftrain_raw):
    ax = dftrain_raw['Survived'].value_counts().plot(kind='bar', figsize=(12, 8), fontsize=15, rot=0)
    ax.set_ylabel('Counts', fontsize=15)
    ax.set_xlabel('Survived', fontsize=15)
    plt.show()


# 年龄分布直方图
def age_png(dftrain_raw):
    ax = dftrain_raw['Age'].plot(kind='hist', bins=20, color='purple', figsize=(12, 8), fontsize=15)
    ax.set_ylabel('Frequency', fontsize=15)
    ax.set_xlabel('Age', fontsize=15)
    plt.show()


# 正态分布
def survived_png2(dftrain_raw):
    ax = dftrain_raw.query('Survived == 0')['Age'].plot(kind='density', figsize=(12, 8), fontsize=15)
    dftrain_raw.query('Survived == 1')['Age'].plot(kind='density', figsize=(12, 8), fontsize=15)
    ax.legend(['Survived==0', 'Survived==1'], fontsize=12)
    ax.set_ylabel('Density', fontsize=15)
    ax.set_xlabel('Age', fontsize=15)
    plt.show()


# 数据预处理
def preprocessing(dfdata):
    dfresult = pd.DataFrame()

    # Pclass
    dfPclass = pd.get_dummies(dfdata['Pclass'])
    dfPclass.columns = ['Pclass_' + str(x) for x in dfPclass.columns]
    dfresult = pd.concat([dfresult, dfPclass], axis=1)

    # Sex
    dfSex = pd.get_dummies(dfdata['Sex'])
    dfresult = pd.concat([dfresult, dfSex], axis=1)

    # Age
    dfresult['Age'] = dfdata['Age'].fillna(0)
    dfresult['Age_null'] = pd.isna(dfdata['Age']).astype('int32')

    # SibSp,Parch,Fare
    dfresult['SibSp'] = dfdata['SibSp']
    dfresult['Parch'] = dfdata['Parch']
    dfresult['Fare'] = dfdata['Fare']

    # Carbin
    dfresult['Cabin_null'] = pd.isna(dfdata['Cabin']).astype('int32')

    # Embarked
    dfEmbarked = pd.get_dummies(dfdata['Embarked'], dummy_na=True)
    dfEmbarked.columns = ['Embarked_' + str(x) for x in dfEmbarked.columns]
    dfresult = pd.concat([dfresult, dfEmbarked], axis=1)

    return (dfresult)


def model_train(model, x_train, y_train):
    # 二分类问题选择二元交叉熵损失函数
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['AUC']
    )

    history = model.fit(
        x_train, y_train,
        batch_size=64,
        epochs=30,
        validation_split=0.2  # 分割一部分训练数据用于验证
    )

    return model, history


# 评估模型
def plot_metric(history, metric):
    train_metrics = history.history[metric]
    val_metrics = history.history['val_' + metric]
    epochs = range(1, len(train_metrics) + 1)
    plt.plot(epochs, train_metrics, 'bo--')
    plt.plot(epochs, val_metrics, 'ro-')
    plt.title('Training and validation ' + metric)
    plt.xlabel("Epochs")
    plt.ylabel(metric)
    plt.legend(["train_" + metric, 'val_' + metric])
    plt.show()


def load_data():
    # 训练数据
    dftrain_raw = pd.read_csv('./data/titanic/train.csv')
    # 测试数据
    dftest_raw = pd.read_csv('./data/titanic/test.csv')
    # 打印前10行数据
    print(dftrain_raw.head(10))
    return dftrain_raw, dftest_raw


def create_model():
    tf.keras.backend.clear_session()

    # 此处选择使用最简单的Sequential，按层顺序模型。
    model = models.Sequential()
    model.add(layers.Dense(20, activation='relu', input_shape=(15,)))
    model.add(layers.Dense(10, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.summary()

    return model


def save_and_use1(model, x_test, y_test):
    model.save('./temp/keras_model.h5')
    del model  # 删除现有模型
    # identical to the previous one
    model = models.load_model('./temp/keras_model.h5')
    print("------------------------------------------------------")
    print(model.evaluate(x_test, y_test))


def save_and_use2(model, x_test, y_test):
    model.save_weights('./temp/tf_model_weights.ckpt', save_format="tf")
    model.save('./temp/tf_model_savedmodel', save_format="tf")
    print('export saved model.')

    model_loaded = tf.keras.models.load_model('./temp/tf_model_savedmodel')
    print("------------------------------------------------------")
    print(model_loaded.evaluate(x_test, y_test))


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    # 加载数据
    dftrain_raw, dftest_raw = load_data()
    # 简单数据查看
    # survived_png(dftrain_raw)
    # survived_png2(dftrain_raw)
    # age_png(dftrain_raw)

    #  数据预处理
    x_train = preprocessing(dftrain_raw)
    y_train = dftrain_raw['Survived'].values
    x_test = preprocessing(dftest_raw)
    y_test = dftest_raw['Survived'].values
    print("x_train.shape =", x_train.shape)
    print("x_test.shape =", x_test.shape)

    # 建立模型
    model = create_model()
    # 模型训练
    model, history = model_train(model, x_train, y_train)
    # 模型评估
    plot_metric(history, "loss")
    # 测试集
    model.evaluate(x=x_test, y=y_test)
    # 预测概率
    print(model.predict(x_test[0:10]))
    # model(tf.constant(x_test[0:10].values,dtype = tf.float32)) #等价写法

    # 结果保存或使用
    # 方式一：Keras方式保存
    # save_and_use1(model, x_test, y_test)
    # 方式二：TensorFlow原生方式保存
    save_and_use2(model, x_test, y_test)
