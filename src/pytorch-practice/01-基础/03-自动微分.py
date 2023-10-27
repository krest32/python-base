import datetime

import numpy as np
import torch


def print_bar(n):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========================", n, "============================" + "%s" % now_time)


def fun1():
    # f(x) = a*x**2 + b*x + c的导数
    x = torch.tensor(0.0, requires_grad=True)  # x需要被求导
    a = torch.tensor(1.0)
    b = torch.tensor(-2.0)
    c = torch.tensor(1.0)
    y = a * torch.pow(x, 2) + b * x + c

    y.backward()
    dy_dx = x.grad
    print(dy_dx)


def fun2():
    # f(x) = a*x**2 + b*x + c
    x = torch.tensor([[0.0, 0.0], [1.0, 2.0]], requires_grad=True)  # x需要被求导
    a = torch.tensor(1.0)
    b = torch.tensor(-2.0)
    c = torch.tensor(1.0)
    y = a * torch.pow(x, 2) + b * x + c

    gradient = torch.tensor([[1.0, 1.0], [1.0, 1.0]])

    print("x:\n", x)
    print("y:\n", y)
    y.backward(gradient=gradient)
    x_grad = x.grad
    print("x_grad:\n", x_grad)


def fun3():
    x = torch.tensor([[0.0, 0.0], [1.0, 2.0]], requires_grad=True)  # x需要被求导
    a = torch.tensor(1.0)
    b = torch.tensor(-2.0)
    c = torch.tensor(1.0)
    y = a * torch.pow(x, 2) + b * x + c

    gradient = torch.tensor([[1.0, 1.0], [1.0, 1.0]])
    z = torch.sum(y * gradient)

    print("x:", x)
    print("y:", y)
    z.backward()
    x_grad = x.grad
    print("x_grad:\n", x_grad)


def fun4():
    # f(x) = a*x**2 + b*x + c的导数
    x = torch.tensor(0.0, requires_grad=True)  # x需要被求导
    a = torch.tensor(1.0)
    b = torch.tensor(-2.0)
    c = torch.tensor(1.0)
    y = a * torch.pow(x, 2) + b * x + c

    # create_graph 设置为 True 将允许创建更高阶的导数
    dy_dx = torch.autograd.grad(y, x, create_graph=True)[0]
    print(dy_dx.data)

    # 求二阶导数
    dy2_dx2 = torch.autograd.grad(dy_dx, x)[0]
    print(dy2_dx2.data)


def fun5():
    x1 = torch.tensor(1.0, requires_grad=True)  # x需要被求导
    x2 = torch.tensor(2.0, requires_grad=True)

    y1 = x1 * x2
    y2 = x1 + x2

    # 允许同时对多个自变量求导数
    (dy1_dx1, dy1_dx2) = torch.autograd.grad(outputs=y1, inputs=[x1, x2], retain_graph=True)
    print(dy1_dx1, dy1_dx2)

    # 如果有多个因变量，相当于把多个因变量的梯度结果求和
    (dy12_dx1, dy12_dx2) = torch.autograd.grad(outputs=[y1, y2], inputs=[x1, x2])
    print(dy12_dx1, dy12_dx2)


def func6():
    x = torch.tensor(0.0, requires_grad=True)  # x需要被求导
    a = torch.tensor(1.0)
    b = torch.tensor(-2.0)
    c = torch.tensor(1.0)

    optimizer = torch.optim.SGD(params=[x], lr=0.01)

    def f(x):
        result = a * torch.pow(x, 2) + b * x + c
        return (result)

    for i in range(500):
        optimizer.zero_grad()
        y = f(x)
        y.backward()
        optimizer.step()

    print("y=", f(x).data, ";", "x=", x.data)


if __name__ == '__main__':
    """
    利用backward方法求导数¶
        backward 方法通常在一个标量张量上调用，该方法求得的梯度将存在对应自变量张量的grad属性下。
        如果调用的张量非标量，则要传入一个和它同形状 的gradient参数张量。
        相当于用该gradient参数张量与调用张量作向量点乘，得到的标量结果再反向传播。
    """

    # 1. 利用backward方法求导数
    # 标量的反向传播
    fun1()
    print_bar(1)

    # 非标量的反向传播
    fun2()
    print_bar(2)

    # 非标量的反向传播可以用标量的反向传播实现
    fun3()
    print_bar(3)

    # 2. 利用autograd.grad方法求导数
    fun4()
    print_bar(4)

    fun5()
    print_bar(5)

    # 3. 利用自动微分和优化器求最小值
    func6()
    print_bar(6)
