import torch
import torchvision
import torchkeras
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms as T
from torchvision import datasets
from matplotlib import pyplot as plt
import os, sys, time
import numpy as np
import pandas as pd
import datetime
from tqdm import tqdm
from copy import deepcopy
from torchkeras.metrics import Accuracy


# 打印时间
def print_bar():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % now_time)


def transform_label(x):
    return torch.tensor([x]).float()


def load_data(transform_img):
    ds_train = datasets.ImageFolder(
        "./data/cifar2/train/",
        transform=transform_img,
        target_transform=transform_label
    )
    ds_val = datasets.ImageFolder(
        "./data/cifar2/test/",
        transform=transform_img,
        target_transform=transform_label
    )

    dl_train = DataLoader(ds_train, batch_size=50, shuffle=True)
    dl_val = DataLoader(ds_val, batch_size=50, shuffle=False)

    return ds_val, ds_train, dl_val, dl_train


def show_data1(ds_train):
    plt.figure(figsize=(8, 8))
    for i in range(9):
        img, label = ds_train[i]
        img = img.permute(1, 2, 0)
        ax = plt.subplot(3, 3, i + 1)
        ax.imshow(img.numpy())
        ax.set_title("label = %d" % label.item())
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5)
        self.dropout = nn.Dropout2d(p=0.1)
        self.adaptive_pool = nn.AdaptiveMaxPool2d((1, 1))
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(64, 32)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(32, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.pool(x)
        x = self.dropout(x)
        x = self.adaptive_pool(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        return x


def show_data2(dl_train):
    for features, labels in dl_train:
        print(features.shape, labels.shape)
        break


def print_log(info):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % now_time)
    print(str(info) + "\n")


class StepRunner:
    def __init__(self, net, loss_fn,
                 stage="train", metrics_dict=None,
                 optimizer=None
                 ):
        self.net, self.loss_fn, self.metrics_dict, self.stage = net, loss_fn, metrics_dict, stage
        self.optimizer = optimizer

    def step(self, features, labels):
        # loss
        preds = self.net(features)
        loss = self.loss_fn(preds, labels)

        # backward()
        if self.optimizer is not None and self.stage == "train":
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()

        # metrics
        step_metrics = {self.stage + "_" + name: metric_fn(preds, labels).item()
                        for name, metric_fn in self.metrics_dict.items()}
        return loss.item(), step_metrics

    def train_step(self, features, labels):
        self.net.train()  # 训练模式, dropout层发生作用
        return self.step(features, labels)

    @torch.no_grad()
    def eval_step(self, features, labels):
        self.net.eval()  # 预测模式, dropout层不发生作用
        return self.step(features, labels)

    def __call__(self, features, labels):
        if self.stage == "train":
            return self.train_step(features, labels)
        else:
            return self.eval_step(features, labels)


class EpochRunner:
    def __init__(self, steprunner):
        self.steprunner = steprunner
        self.stage = steprunner.stage

    def __call__(self, dataloader):
        total_loss, step = 0, 0
        loop = tqdm(enumerate(dataloader), total=len(dataloader))
        for i, batch in loop:
            loss, step_metrics = self.steprunner(*batch)
            step_log = dict({self.stage + "_loss": loss}, **step_metrics)
            total_loss += loss
            step += 1
            if i != len(dataloader) - 1:
                loop.set_postfix(**step_log)
            else:
                epoch_loss = total_loss / step
                epoch_metrics = {self.stage + "_" + name: metric_fn.compute().item()
                                 for name, metric_fn in self.steprunner.metrics_dict.items()}
                epoch_log = dict({self.stage + "_loss": epoch_loss}, **epoch_metrics)
                loop.set_postfix(**epoch_log)

                for name, metric_fn in self.steprunner.metrics_dict.items():
                    metric_fn.reset()
        return epoch_log


def train_model(net, optimizer, loss_fn, metrics_dict,
                train_data, val_data=None,
                epochs=10, ckpt_path='checkpoint.pt',
                patience=5, monitor="val_loss", mode="min"):
    history = {}

    for epoch in range(1, epochs + 1):
        print_log("Epoch {0} / {1}".format(epoch, epochs))

        # 1，train -------------------------------------------------
        train_step_runner = StepRunner(net=net, stage="train",
                                       loss_fn=loss_fn, metrics_dict=deepcopy(metrics_dict),
                                       optimizer=optimizer)
        train_epoch_runner = EpochRunner(train_step_runner)
        train_metrics = train_epoch_runner(train_data)

        for name, metric in train_metrics.items():
            history[name] = history.get(name, []) + [metric]

        # 2，validate -------------------------------------------------
        if val_data:
            val_step_runner = StepRunner(net=net, stage="val",
                                         loss_fn=loss_fn, metrics_dict=deepcopy(metrics_dict))
            val_epoch_runner = EpochRunner(val_step_runner)
            with torch.no_grad():
                val_metrics = val_epoch_runner(val_data)
            val_metrics["epoch"] = epoch
            for name, metric in val_metrics.items():
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

    return pd.DataFrame(history)


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


def predict(net, dl):
    net.eval()
    with torch.no_grad():
        result = nn.Sigmoid()(torch.cat([net.forward(t[0]) for t in dl]))
    return (result.data)


if __name__ == '__main__':
    # mac系统上pytorch和matplotlib在jupyter中同时跑需要更改环境变量
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    print("torch.__version__ = ", torch.__version__)
    print("torchvision.__version__ = ", torchvision.__version__)
    print("torchkeras.__version__ = ", torchkeras.__version__)
    print_bar()

    # 1.1 加载数据
    transform_img = T.Compose([T.ToTensor()])
    ds_val, ds_train, dl_val, dl_train = load_data(transform_img)
    print(ds_train.class_to_idx)

    # 1.2 显示示例数据
    show_data2(dl_train)
    show_data1(ds_train)

    # 2. 定义模型
    pool = nn.AdaptiveMaxPool2d((1, 1))
    t = torch.randn(10, 8, 32, 32)
    print(pool(t).shape)

    net = Net()
    print(net)

    # 3. 训练模型
    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=0.01)
    metrics_dict = {"acc": Accuracy()}

    dfhistory = train_model(
        net,
        optimizer,
        loss_fn,
        metrics_dict,
        train_data=dl_train,
        val_data=dl_val,
        epochs=10,
        patience=3,
        monitor="val_acc",
        mode="max"
    )
    print(dfhistory)

    # 4. 评估模型
    plot_metric(dfhistory, "loss")
    plot_metric(dfhistory, "acc")

    # 5. 使用模型
    # 预测概率
    y_pred_probs = predict(net, dl_val)
    print(y_pred_probs)
    # 预测类别
    y_pred = torch.where(y_pred_probs > 0.5, torch.ones_like(y_pred_probs), torch.zeros_like(y_pred_probs))
    print(y_pred)

    # 6. 保存模型
    print(net.state_dict().keys())
    # 保存模型参数
    torch.save(net.state_dict(), "./net_parameter.pt")
    # 加载模型
    net_clone = Net()
    net_clone.load_state_dict(torch.load("./net_parameter.pt"))
    # 使用模型
    predict(net_clone, dl_val)