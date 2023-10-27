import os
import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import torch
from torch import nn


# 打印时间
def print_bar():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % nowtime)


# mac系统上pytorch和matplotlib在jupyter中同时跑需要更改环境变量
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 样本数量
n = 400

# 生成测试用数据集
X = 10 * torch.rand([n, 2]) - 5.0  # torch.rand是均匀分布
w0 = torch.tensor([[2.0], [-3.0]])
b0 = torch.tensor([[10.0]])
Y = X @ w0 + b0 + torch.normal(0.0, 2.0, size=[n, 1])  # @表示矩阵乘法,增加正态扰动

# 数据可视化
plt.figure(figsize=(12, 5))
ax1 = plt.subplot(121)
ax1.scatter(X[:, 0].numpy(), Y[:, 0].numpy(), c="b", label="samples")
ax1.legend()
plt.xlabel("x1")
plt.ylabel("y", rotation=0)

ax2 = plt.subplot(122)
ax2.scatter(X[:, 1].numpy(), Y[:, 0].numpy(), c="g", label="samples")
ax2.legend()
plt.xlabel("x2")
plt.ylabel("y", rotation=0)
plt.show()


# 构建数据管道迭代器
def data_iter(features, labels, batch_size=8):
    num_examples = len(features)
    indices = list(range(num_examples))
    np.random.shuffle(indices)  # 样本的读取顺序是随机的
    for i in range(0, num_examples, batch_size):
        indexs = torch.LongTensor(indices[i: min(i + batch_size, num_examples)])
        yield features.index_select(0, indexs), labels.index_select(0, indexs)


# 测试数据管道效果
batch_size = 8
(features, labels) = next(data_iter(X, Y, batch_size))
print(features)
print(labels)


# 定义模型
class LinearRegression:

    def __init__(self):
        self.w = torch.randn_like(w0, requires_grad=True)
        self.b = torch.zeros_like(b0, requires_grad=True)

    # 正向传播
    def forward(self, x):
        return x @ self.w + self.b

    # 损失函数
    def loss_func(self, y_pred, y_true):
        return torch.mean((y_pred - y_true) ** 2 / 2)


model = LinearRegression()


def train_step(model, features, labels):
    predictions = model.forward(features)
    loss = model.loss_func(predictions, labels)

    # 反向传播求梯度
    loss.backward()

    # 使用torch.no_grad()避免梯度记录，也可以通过操作 model.w.data 实现避免梯度记录
    with torch.no_grad():
        # 梯度下降法更新参数
        model.w -= 0.001 * model.w.grad
        model.b -= 0.001 * model.b.grad

        # 梯度清零
        model.w.grad.zero_()
        model.b.grad.zero_()
    return loss


# 测试train_step效果
batch_size = 10
(features, labels) = next(data_iter(X, Y, batch_size))
train_step(model, features, labels)


def train_model(model, epochs):
    for epoch in range(1, epochs + 1):
        for features, labels in data_iter(X, Y, 10):
            loss = train_step(model, features, labels)

        if epoch % 200 == 0:
            print_bar()
            print("epoch =", epoch, "loss = ", loss.item())
            print("model.w =", model.w.data)
            print("model.b =", model.b.data)


train_model(model, epochs=1000)

# 结果可视化

plt.figure(figsize=(12, 5))
ax1 = plt.subplot(121)
ax1.scatter(X[:, 0].numpy(), Y[:, 0].numpy(), c="b", label="samples")
ax1.plot(X[:, 0].numpy(), (model.w[0].data * X[:, 0] + model.b[0].data).numpy(), "-r", linewidth=5.0, label="model")
ax1.legend()
plt.xlabel("x1")
plt.ylabel("y", rotation=0)

ax2 = plt.subplot(122)
ax2.scatter(X[:, 1].numpy(), Y[:, 0].numpy(), c="g", label="samples")
ax2.plot(X[:, 1].numpy(), (model.w[1].data * X[:, 1] + model.b[0].data).numpy(), "-r", linewidth=5.0, label="model")
ax2.legend()
plt.xlabel("x2")
plt.ylabel("y", rotation=0)

plt.show()
