import datetime

import numpy as np
import torch


def print_bar(n):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========================", n, "============================" + "%s" % now_time)


if __name__ == '__main__':
    """
    张量的数据类型和numpy.array基本一一对应，但是不支持str类型。
    包括:
    1. torch.float64(torch.double),
    2. torch.float32(torch.float),
    3. torch.float16,
    4. torch.int64(torch.long),
    5. torch.int32(torch.int),
    6. torch.int16,
    7. torch.int8,
    8. torch.uint8,
    9. torch.bool
    一般神经网络建模使用的都是torch.float32类型。
    """
    # 1. 自动推断数据类型
    i = torch.tensor(1);
    print(i, i.dtype)
    x = torch.tensor(2.0);
    print(x, x.dtype)
    b = torch.tensor(True);
    print(b, b.dtype)
    print_bar(1)

    # 2. 指定数据类型
    i = torch.tensor(1, dtype=torch.int32);
    print(i, i.dtype)
    x = torch.tensor(2.0, dtype=torch.double);
    print(x, x.dtype)
    print_bar(2)

    # 3. 使用特定类型构造函数
    i = torch.IntTensor(1);
    print(i, i.dtype)
    x = torch.Tensor(np.array(2.0));
    print(x, x.dtype)  # 等价于torch.FloatTensor
    b = torch.BoolTensor(np.array([1, 0, 2, 0]));
    print(b, b.dtype)
    print_bar(3)

    # 4. 不同类型进行转换
    i = torch.tensor(1);
    print(i, i.dtype)
    x = i.float();
    print(x, x.dtype)  # 调用 float方法转换成浮点类型
    y = i.type(torch.float);
    print(y, y.dtype)  # 使用type函数转换成浮点类型
    z = i.type_as(x);
    print(z, z.dtype)  # 使用type_as方法转换成某个Tensor相同类型
    print_bar(5)

    """
    不同类型的数据可以用不同维度(dimension)的张量来表示。
    1. 标量为0维张量，向量为1维张量，矩阵为2维张量。
    2. 彩色图像有rgb三个通道，可以表示为3维张量。
    3. 视频还有时间维，可以表示为4维张量。
    可以简单地总结为：有几层中括号，就是多少维的张量。
    """
    scalar = torch.tensor(True)
    print(scalar)
    print(scalar.dim())  # 标量，0维张量
    print_bar(6)

    vector = torch.tensor([1.0, 2.0, 3.0, 4.0])  # 向量，1维张量
    print(vector)
    print(vector.dim())
    print_bar(7)

    matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])  # 矩阵, 2维张量
    print(matrix)
    print(matrix.dim())
    print_bar(8)

    tensor3 = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])  # 3维张量
    print(tensor3)
    print(tensor3.dim())
    print_bar(9)

    tensor4 = torch.tensor([[[[1.0, 1.0], [2.0, 2.0]], [[3.0, 3.0], [4.0, 4.0]]],
                            [[[5.0, 5.0], [6.0, 6.0]], [[7.0, 7.0], [8.0, 8.0]]]])  # 4维张量
    print(tensor4)
    print(tensor4.dim())
    print_bar(10)

    """
    张量的尺寸
    1. 可以使用 shape 属性或者 size()方法查看张量在每一维的长度.
    2. 可以使用view方法改变张量的尺寸。
    3. 如果view方法改变尺寸失败，可以使用reshape方法.
    """
    scalar = torch.tensor(True)
    print(scalar.size())
    print(vector.shape)
    print_bar(11)

    vector = torch.tensor([1.0, 2.0, 3.0, 4.0])
    print(vector.size())
    print(vector.shape)
    print_bar(12)

    matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    print(matrix.size())
    print_bar(13)

    # 使用view可以改变张量尺寸
    vector = torch.arange(0, 12)
    print(vector)
    print(vector.shape)

    matrix34 = vector.view(3, 4)
    print(matrix34)
    print(matrix34.shape)

    matrix43 = vector.view(4, -1)  # -1表示该位置长度由程序自动推断
    print(matrix43)
    print(matrix43.shape)
    print_bar(14)

    # 有些操作会让张量存储结构扭曲，直接使用view会失败，可以用reshape方法
    matrix26 = torch.arange(0, 12).view(2, 6)
    print(matrix26)
    print(matrix26.shape)

    # 转置操作让张量存储结构扭曲
    matrix62 = matrix26.t()
    print(matrix62.is_contiguous())

    # 直接使用view方法会失败，可以使用reshape方法
    # matrix34 = matrix62.view(3,4) #error!
    matrix34 = matrix62.reshape(3, 4)  # 等价于matrix34 = matrix62.contiguous().view(3,4)
    print(matrix34)
    print_bar(15)

    # torch.from_numpy函数从numpy数组得到Tensor

    arr = np.zeros(3)
    tensor = torch.from_numpy(arr)
    print("before add 1:")
    print(arr)
    print(tensor)

    print("\nafter add 1:")
    np.add(arr, 1, out=arr)  # 给 arr增加1，tensor也随之改变
    print(arr)
    print(tensor)
    print_bar(16)

    # numpy方法从Tensor得到numpy数组

    tensor = torch.zeros(3)
    arr = tensor.numpy()
    print("before add 1:")
    print(tensor)
    print(arr)

    print("\nafter add 1:")

    # 使用带下划线的方法表示计算结果会返回给调用 张量
    tensor.add_(1)  # 给 tensor增加1，arr也随之改变
    # 或： torch.add(tensor,1,out = tensor)
    print(tensor)
    print(arr)
    print_bar(17)

    # 可以用clone() 方法拷贝张量，中断这种关联

    tensor = torch.zeros(3)

    # 使用clone方法拷贝张量, 拷贝后的张量和原始张量内存独立
    arr = tensor.clone().numpy()  # 也可以使用tensor.data.numpy()
    print("before add 1:")
    print(tensor)
    print(arr)

    print("\nafter add 1:")

    # 使用 带下划线的方法表示计算结果会返回给调用 张量
    tensor.add_(1)  # 给 tensor增加1，arr不再随之改变
    print(tensor)
    print(arr)
    print_bar(18)

    # item 方法和 tolist 方法可以将张量转换成Python数值和数值列表
    scalar = torch.tensor(1.0)
    s = scalar.item()
    print(s)
    print(type(s))

    tensor = torch.rand(2, 2)
    t = tensor.tolist()
    print(t)
    print(type(t))
    print_bar(19)

    # torch.normal()是PyTorch中用于生成服从正态分布的随机数的函数。
    """
    参数说明
    1. mean：正态分布的均值。可以是一个数值或一个张量。
    2. std：正态分布的标准差。可以是一个数值或一个张量。
    3. size：输出随机数的形状。可以是一个整数，用于生成一个大小为(size,)的一维张量；也可以是一个元组，用于生成相应形状的多维张量。
    4. out：可选参数，用于指定一个输出张量。
    """
    print(torch.normal(0.0, 2.0, size=[n, 1]))