import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader, TensorDataset

import sys, time
import datetime
from tqdm import tqdm

from copy import deepcopy
from torchkeras.metrics import Accuracy

# mac系统上pytorch和matplotlib在jupyter中同时跑需要更改环境变量
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import torchkeras

"""
数据字段说明：
    Survived:0代表死亡，1代表存活【y标签】
    Pclass:乘客所持票类，有三种值(1,2,3) 【转换成onehot编码】
    Name:乘客姓名 【舍去】
    Sex:乘客性别 【转换成bool特征】
    Age:乘客年龄(有缺失) 【数值特征，添加“年龄是否缺失”作为辅助特征】
    SibSp:乘客兄弟姐妹/配偶的个数(整数值) 【数值特征】
    Parch:乘客父母/孩子的个数(整数值)【数值特征】
    Ticket:票号(字符串)【舍去】
    Fare:乘客所持票的价格(浮点数，0-500不等) 【数值特征】
    Cabin:乘客所在船舱(有缺失) 【添加“所在船舱是否缺失”作为辅助特征】
    Embarked:乘客登船港口:S、C、Q(有缺失)【转换成onehot编码，四维度 S,C,Q,nan】
"""


def load_data():
    dftrain_raw = pd.read_csv('./data/titanic/train.csv')
    dftest_raw = pd.read_csv('./data/titanic/test.csv')
    return dftrain_raw, dftest_raw


def show_data1(dftrain_raw):
    ax = dftrain_raw['Survived'].value_counts().plot(kind='bar', figsize=(12, 8), fontsize=15, rot=0)
    ax.set_ylabel('Counts', fontsize=15)
    ax.set_xlabel('Survived', fontsize=15)
    plt.show()


def show_data2(dftrain_raw):
    ax = dftrain_raw.query('Survived == 0')['Age'].plot(kind='density', figsize=(12, 8), fontsize=15)
    dftrain_raw.query('Survived == 1')['Age'].plot(kind='density', figsize=(12, 8), fontsize=15)
    ax.legend(['Survived==0', 'Survived==1'], fontsize=12)
    ax.set_ylabel('Density', fontsize=15)
    ax.set_xlabel('Age', fontsize=15)
    plt.show()


def show_data3(dftrain_raw):
    ax = dftrain_raw['Age'].plot(kind='hist', bins=20, color='purple', figsize=(12, 8), fontsize=15)
    ax.set_ylabel('Frequency', fontsize=15)
    ax.set_xlabel('Age', fontsize=15)
    plt.show()


# 正式的数据预处理
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


def dataPerProcess(dftrain_raw, dftest_raw):
    x_train = preprocessing(dftrain_raw).values
    y_train = dftrain_raw[['Survived']].values

    x_test = preprocessing(dftest_raw).values
    y_test = dftest_raw[['Survived']].values

    print("x_train.shape =", x_train.shape)
    print("x_test.shape =", x_test.shape)

    print("y_train.shape =", y_train.shape)
    print("y_test.shape =", y_test.shape)
    return x_test, y_test, x_train, y_train


# 定义模型
def create_net():
    net = nn.Sequential()
    net.add_module("linear1", nn.Linear(15, 20))
    net.add_module("relu1", nn.ReLU())
    net.add_module("linear2", nn.Linear(20, 15))
    net.add_module("relu2", nn.ReLU())
    net.add_module("linear3", nn.Linear(15, 1))
    print(net)
    return net


# 训练模型

def printlog(info):
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % nowtime)
    print(str(info) + "\n")


def train_model(net, x_train, y_train):

    dl_train = DataLoader(
        TensorDataset(
            torch.tensor(x_train).float(),
            torch.tensor(y_train).float()
        ),
        shuffle=True,
        batch_size=8
    )
    dl_val = DataLoader(
        TensorDataset(
            torch.tensor(x_test).float(),
            torch.tensor(y_test).float()
        ),
        shuffle=False,
        batch_size=8
    )

    # 测试数据管道
    for features, labels in dl_train:
        print(features, labels)
        break

    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=0.01)
    metrics_dict = {"acc": Accuracy()}

    epochs = 20
    ckpt_path = 'checkpoint.pt'

    # early_stopping相关设置
    monitor = "val_acc"
    patience = 5
    mode = "max"

    history = {}

    for epoch in range(1, epochs + 1):
        printlog("Epoch {0} / {1}".format(epoch, epochs))

        # 1，train -------------------------------------------------
        net.train()

        total_loss, step = 0, 0

        loop = tqdm(enumerate(dl_train), total=len(dl_train), file=sys.stdout)
        train_metrics_dict = deepcopy(metrics_dict)

        for i, batch in loop:

            features, labels = batch
            # forward
            preds = net(features)
            loss = loss_fn(preds, labels)

            # backward
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            # metrics
            step_metrics = {"train_" + name: metric_fn(preds, labels).item()
                            for name, metric_fn in train_metrics_dict.items()}

            step_log = dict({"train_loss": loss.item()}, **step_metrics)

            total_loss += loss.item()

            step += 1
            if i != len(dl_train) - 1:
                loop.set_postfix(**step_log)
            else:
                epoch_loss = total_loss / step
                epoch_metrics = {"train_" + name: metric_fn.compute().item()
                                 for name, metric_fn in train_metrics_dict.items()}
                epoch_log = dict({"train_loss": epoch_loss}, **epoch_metrics)
                loop.set_postfix(**epoch_log)

                for name, metric_fn in train_metrics_dict.items():
                    metric_fn.reset()

        for name, metric in epoch_log.items():
            history[name] = history.get(name, []) + [metric]

        # 2，validate -------------------------------------------------
        net.eval()

        total_loss, step = 0, 0
        loop = tqdm(enumerate(dl_val), total=len(dl_val), file=sys.stdout)

        val_metrics_dict = deepcopy(metrics_dict)

        with torch.no_grad():
            for i, batch in loop:

                features, labels = batch

                # forward
                preds = net(features)
                loss = loss_fn(preds, labels)

                # metrics
                step_metrics = {"val_" + name: metric_fn(preds, labels).item()
                                for name, metric_fn in val_metrics_dict.items()}

                step_log = dict({"val_loss": loss.item()}, **step_metrics)

                total_loss += loss.item()
                step += 1
                if i != len(dl_val) - 1:
                    loop.set_postfix(**step_log)
                else:
                    epoch_loss = (total_loss / step)
                    epoch_metrics = {"val_" + name: metric_fn.compute().item()
                                     for name, metric_fn in val_metrics_dict.items()}
                    epoch_log = dict({"val_loss": epoch_loss}, **epoch_metrics)
                    loop.set_postfix(**epoch_log)

                    for name, metric_fn in val_metrics_dict.items():
                        metric_fn.reset()

        epoch_log["epoch"] = epoch
        for name, metric in epoch_log.items():
            history[name] = history.get(name, []) + [metric]

        # 3，early-stopping -------------------------------------------------
        arr_scores = history[monitor]
        best_score_idx = np.argmax(arr_scores) if mode == "max" else np.argmin(arr_scores)
        if best_score_idx == len(arr_scores) - 1:
            torch.save(net.state_dict(), ckpt_path)
            print("<<<<<< reach best {0} : {1} >>>>>>".format(monitor,
                                                              arr_scores[best_score_idx]), file=sys.stderr)
        if len(arr_scores) - best_score_idx > patience:
            print("<<<<<< {} without improvement in {} epoch, early stopping >>>>>>".format(
                monitor, patience), file=sys.stderr)
            break
        net.load_state_dict(torch.load(ckpt_path))

    dfhistory = pd.DataFrame(history)

    # 评估模型
    print(dfhistory)
    return dfhistory, metric


# 评估模型
def plot_metric(dfhistory, metric):
    train_metrics = dfhistory["train_" + metric]
    val_metrics = dfhistory['val_' + metric]
    epochs = range(1, len(train_metrics) + 1)
    plt.plot(epochs, train_metrics, 'bo--')
    plt.plot(epochs, val_metrics, 'ro-')
    plt.title('Training and validation ' + metric)
    plt.xlabel("Epochs")
    plt.ylabel(metric)
    plt.legend(["train_" + metric, 'val_' + metric])
    plt.show()


if __name__ == '__main__':
    print("torch.__version__ = ", torch.__version__)
    print("torchkeras.__version__ = ", torchkeras.__version__)

    # 准备数据
    dftrain_raw, dftest_raw = load_data()
    show_data1(dftrain_raw)
    show_data2(dftrain_raw)
    show_data3(dftrain_raw)

    # 数据预处理
    x_test, y_test, x_train, y_train = dataPerProcess(dftrain_raw, dftest_raw)

    # 定义模型
    net = create_net()

    # 训练模型
    dfhistory, metric = train_model(net, x_train, y_train)

    # 评估模型
    plot_metric(dfhistory, "loss")
    plot_metric(dfhistory, "acc")

    # 使用模型
    y_pred_probs = torch.sigmoid(net(torch.tensor(x_test[0:10]).float())).data
    print(y_pred_probs)
    # 预测类别
    y_pred = torch.where(y_pred_probs > 0.5, torch.ones_like(y_pred_probs), torch.zeros_like(y_pred_probs))
    print(y_pred)

    # 保存模型
    print(net.state_dict().keys())
    # 保存模型参数

    torch.save(net.state_dict(), "./data/net_parameter.pt")
    net_clone = create_net()
    net_clone.load_state_dict(torch.load("./data/net_parameter.pt"))
    torch.sigmoid(net_clone.forward(torch.tensor(x_test[0:10]).float())).data
