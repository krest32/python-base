import torch
from matplotlib import pyplot as plt

if __name__ == '__main__':
    n = 400
    # 生成 n * 2 的矩阵数组，其中每个数字 * 10, 然后 - 5
    x_data = 10 * torch.rand([n, 2]) - 5.0
    # 数据的维度
    print(x_data.shape)
    # 2 * 1 的矩阵
    w0 = torch.tensor(
        [
            [2.0],
            [-3.0]
        ]
    )
    print(w0.shape)
    b0 = torch.tensor(
        [
            [10.0]
        ]
    )
    print(b0.shape)
    # 根据公式得到 y 的值
    # torch.normal 说明 生成一个 n * 1 的正态分布随机数矩阵， 其中平均数为 0.0，标准差为 2.0
    y_data = x_data @ w0 + b0 + torch.normal(0.0, 2.0, size=[n, 1])
    print(y_data.shape)

    # 设置显示图形的大小
    plt.figure(figsize=(18, 7))

    # 第一个图像
    ax1 = plt.subplot(121)
    ax1.scatter(x_data[:, 0].numpy(), y_data[:, 0].numpy(), c="b", label="samples")
    ax1.legend()
    plt.xlabel("x1")
    plt.ylabel("y", rotation=0)

    # 第二个图像
    ax2 = plt.subplot(122)
    ax2.scatter(x_data[:, 1].numpy(), y_data[:, 0].numpy(), c="g", label="samples")
    ax2.legend()
    plt.xlabel("x2")
    plt.ylabel("y", rotation=0)
    plt.show()
