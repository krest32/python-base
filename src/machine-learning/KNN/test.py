import knn

if __name__ == '__main__':
    group, label = knn.create_data_set()
    print(knn.classify([0, 0], group, label, 3))
