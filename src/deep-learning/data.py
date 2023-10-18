import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np

# 加载数据集
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# 输出数据形状
train_images.shape, test_images.shape

# 设置窗口大小为 20*12 单位英寸
plt.figure(figsize=(20, 12))

for i in range(20):
    # 设置子图行数为5，列数为10，i+1表示第几个子图
    plt.subplot(5, 10, i + 1)

    # 去掉坐标轴刻度
    plt.xticks([])
    plt.yticks([])

    # 显示图片
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # 显示标签
    plt.xlabel(train_labels[i])
plt.show()

# 调整数据到我们需要的格式
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

model = models.Sequential([  #
    layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1)),  # 卷积层：提取图片特征
    layers.Flatten(),  # Flatten层：将二维图片压缩为一维形式
    layers.Dense(100),  # 全连接层：将特征进行进一步压缩
    layers.Dense(10)  # 输出层：输出结果
])

# 打印网络结构
model.summary()

model.compile(optimizer='adam',  # adam是优化器的一种
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  # 损失函数的一种计算方法
              metrics=['accuracy'])  # 采用准确率来评价模型

"""
train_images   ：训练数据的图片
train_labels   ：训练图片对应的标签
epochs         ：训练轮数
validation_data：验证数据
"""
history = model.fit(
    train_images,
    train_labels,
    epochs=3,
    validation_data=(test_images, test_labels)
)

plt.imshow(test_images[1])
pre = model.predict(test_images)
pre[1]

np.array(
    [12.474585, 1.1173537, 21.654232, 16.206923, -10.989567, 17.235504, 19.404213, -22.553476, 13.221286, -10.19972],
    dtype=float
)

# 输出预测结果
pre_num = np.argmax(pre[1])
print("模型的预测结果为：", pre_num)
