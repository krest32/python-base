"""
tensorflow-base-serving
TensorFlow Lite
　　TensorFlow Lite 是 TensorFlow 在移动和 IoT 等边缘设备端的解决方案，提供了 Java、Python 和 C++ API 库，可以运行在 Android、iOS 和 Raspberry Pi 等设备上。AI技术在边缘设备上的应用，TFLite 将会是愈发重要的角色。

　　目前 TFLite 只提供了推理功能，在服务器端进行训练后，经过如下简单处理即可部署到边缘设备上。

模型转换：由于边缘设备计算等资源有限，使用 TensorFlow 训练好的模型，模型太大、运行效率比较低，不能直接在移动端部署，需要通过相应工具进行转换成适合边缘设备的格式。
边缘设备部署：本节以 android 为例，简单介绍如何在 android 应用中部署转化后的模型，完成 Mnist 图片的识别。
"""