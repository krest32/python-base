import knn

if __name__ == '__main__':
    group, label = knn.create_data_set()
    # 分类的点、观测数组、观测数组分类，K值
    print(knn.classify([0, 0], group, label, 3))
