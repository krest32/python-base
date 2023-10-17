from numpy import *  # 科学计算包numpy
import operator  # 运算符模块


def create_data_set():  # 创建数据集和标签
    group = array(
        [
            [1.0, 1.1],
            [1.0, 1.0],
            [0, 0.2],
            [0, 0.1]
        ]
    )
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(input, data_set, labels, k):
    # 用于分类的输入向量inX，输入的训练样本集dataSet，标签向量labels，k表示用于选择最近邻居的数目
    data_set_size = data_set.shape[0]
    # 数组中一共有多少个点
    print(data_set_size)
    # 距离计算，使用欧式距离公式
    diff_mat = tile(input, (data_set_size, 1)) - data_set
    aq_diff_mat = diff_mat ** 2
    aq_distances = aq_diff_mat.sum(axis=1)
    distances = aq_distances ** 0.5
    sorted_dist = distances.argsort()

    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1  # 选择距离最小的k个点

    # iteritems 用于python2
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)  # 排序
    return sorted_class_count[0][0]
