import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import torch
from torch import nn

if __name__ == '__main__':
    # 正负样本数量
    n_positive, n_negative = 2000, 2000
    # 生成正样本, 小圆环分布
    r_p = 5.0 + torch.normal(0.0, 1.0, size=[n_positive, 1])
    theta_p = 2 * np.pi * torch.rand([n_positive, 1])
    Xp = torch.cat([r_p * torch.cos(theta_p), r_p * torch.sin(theta_p)], axis=1)
    Yp = torch.ones_like(r_p)

    # 生成负样本, 大圆环分布
    r_n = 8.0 + torch.normal(0.0, 1.0, size=[n_negative, 1])
    theta_n = 2 * np.pi * torch.rand([n_negative, 1])
    Xn = torch.cat([r_n * torch.cos(theta_n), r_n * torch.sin(theta_n)], axis=1)
    Yn = torch.zeros_like(r_n)

    # 汇总样本
    X = torch.cat([Xp, Xn], axis=0)
    Y = torch.cat([Yp, Yn], axis=0)

    # 可视化
    plt.figure(figsize=(6, 6))
    plt.scatter(Xp[:, 0].numpy(), Xp[:, 1].numpy(), c="r")
    plt.scatter(Xn[:, 0].numpy(), Xn[:, 1].numpy(), c="g")
    plt.legend(["positive", "negative"]);
