🔥🔥 B站视频讲解：https://www.bilibili.com/video/BV1Ua411P7oe

🍉🍉 项目github地址：https://github.com/lyhue1991/eat_pytorch_in_20_days

🐳🐳 项目和鲸专栏地址：https://www.kesci.com/home/column/5f2ac5d8af3980002cb1bc08

### 一、Pytorch的建模流程

使用Pytorch实现神经网络模型的一般流程包括：

1，准备数据

2，定义模型

3，训练模型

4，评估模型

5，使用模型

6，保存模型。

对新手来说，其中最困难的部分实际上是准备数据过程。

我们在实践中通常会遇到的数据类型包括结构化数据，图片数据，文本数据，时间序列数据。

我们将分别以titanic生存预测问题，cifar2图片分类问题，imdb电影评论分类问题，国内新冠疫情结束时间预测问题为例，演示应用Pytorch对这四类数据的建模方法。
### 二、Pytorch的核心概念
Pytorch是一个基于Python的机器学习库。它广泛应用于计算机视觉，自然语言处理等深度学习领域。是目前和TensorFlow分庭抗礼的深度学习框架，在学术圈颇受欢迎。

它主要提供了以下两种核心功能：

1，支持GPU加速的张量计算。

2，方便优化模型的自动微分机制。

Pytorch的主要优点：

简洁易懂：Pytorch的API设计的相当简洁一致。基本上就是tensor, autograd, nn三级封装。学习起来非常容易。有一个这样的段子，说TensorFlow的设计哲学是 Make it complicated, Keras 的设计哲学是 Make it complicated and hide it, 而Pytorch的设计哲学是 Keep it simple and stupid.

便于调试：Pytorch采用动态图，可以像普通Python代码一样进行调试。不同于TensorFlow, Pytorch的报错说明通常很容易看懂。有一个这样的段子，说你永远不可能从TensorFlow的报错说明中找到它出错的原因。

强大高效：Pytorch提供了非常丰富的模型组件，可以快速实现想法。并且运行速度很快。目前大部分深度学习相关的Paper都是用Pytorch实现的。有些研究人员表示，从使用TensorFlow转换为使用Pytorch之后，他们的睡眠好多了，头发比以前浓密了，皮肤也比以前光滑了。

俗话说，万丈高楼平地起，Pytorch这座大厦也有它的地基。

Pytorch底层最核心的概念是张量，动态计算图以及自动微分。

### 三、Pytorch的层次结构
本章我们介绍Pytorch中5个不同的层次结构：即硬件层，内核层，低阶API，中阶API，高阶API【torchkeras】。并以线性回归和DNN二分类模型为例，直观对比展示在不同层级实现模型的特点。

Pytorch的层次结构从低到高可以分成如下五层。

最底层为硬件层，Pytorch支持CPU、GPU加入计算资源池。

第二层为C++实现的内核。

第三层为Python实现的操作符，提供了封装C++内核的低级API指令，主要包括各种张量操作算子、自动微分、变量管理. 如torch.tensor,torch.cat,torch.autograd.grad,nn.Module. 如果把模型比作一个房子，那么第三层API就是【模型之砖】。

第四层为Python实现的模型组件，对低级API进行了函数封装，主要包括各种模型层，损失函数，优化器，数据管道等等。 如torch.nn.Linear,torch.nn.BCE,torch.optim.Adam,torch.utils.data.DataLoader. 如果把模型比作一个房子，那么第四层API就是【模型之墙】。

第五层为Python实现的模型接口。Pytorch没有官方的高阶API。为了便于训练模型，作者仿照keras中的模型接口，使用了不到300行代码，封装了Pytorch的高阶模型接口torchkeras.Model。如果把模型比作一个房子，那么第五层API就是模型本身，即【模型之屋】。

### 四、Pytorch的低阶API
Pytorch的低阶API主要包括张量操作，动态计算图和自动微分。

如果把模型比作一个房子，那么低阶API就是【模型之砖】。

在低阶API层次上，可以把Pytorch当做一个增强版的numpy来使用。

Pytorch提供的方法比numpy更全面，运算速度更快，如果需要的话，还可以使用GPU进行加速。

前面几章我们对低阶API已经有了一个整体的认识，本章我们将重点详细介绍张量操作和动态计算图。

张量的操作主要包括张量的结构操作和张量的数学运算。

张量结构操作诸如：张量创建，索引切片，维度变换，合并分割。

张量数学运算主要有：标量运算，向量运算，矩阵运算。另外我们会介绍张量运算的广播机制。

动态计算图我们将主要介绍动态计算图的特性，计算图中的Function，计算图与反向传播。

### 五、Pytorch的中阶API
我们将主要介绍Pytorch的如下中阶API

数据管道

模型层

损失函数

TensorBoard可视化

如果把模型比作一个房子，那么中阶API就是【模型之墙】。

### 六、Pytorch的高阶API
Pytorch没有官方的高阶API。一般通过nn.Module来构建模型并编写自定义训练循环。

为了更加方便地训练模型，作者编写了仿keras的Pytorch模型接口：torchkeras， 作为Pytorch的高阶API。

本章我们主要详细介绍Pytorch的高阶API如下相关的内容。

构建模型的3种方法(继承nn.Module基类，使用nn.Sequential，辅助应用模型容器)

训练模型的3种方法(脚本风格，函数风格，torchkeras.Model类风格)

使用GPU训练模型(单GPU训练，多GPU训练)

### 七、Pytorch与广告推荐
根据业务和技术方向的差异性，目前工业界的算法工程师主要可以分成 广告算法工程师、推荐算法工程师、风控算法工程师、CV算法工程师、NLP算法工程师、 等等。

除了一些多模态数据外(文本、图像、社交网络等)，广告算法工程师、推荐算法工程师、风控算法工程师处理的数据类型主要还是是结构化数据，

风控领域目前工业界用到的模型还是树模型为主，广告和推荐领域目前工业界是深度模型为主。

由于数据结构的相似性，广告的CTR预估模型和推荐系统的精排模型，基本是通用的。

本章将首先概述推荐算法和广告算法的基础业务知识，然后深入了解一些经典的CTR预估/精排模型，并在Criteo数据集或者Movielens数据集上演示完整范例。

包括：FM、DeepFM、FiBiNET、DeepCross、DIN、DIEN。