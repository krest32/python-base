
if __name__ == '__main__':
    word_count={}
    with open("English.txt", 'r', encoding='utf-8-sig') as fin:
        for line in fin:
            line = line[:-1]
            # 按照空格进行分割单词
            words = line.split()
            for word in words:
                # 如果遍历的单词不在字典中，那么将单词加入到字典中
                if word not in word_count:
                    word_count[word] = 0;
                word_count[word] += 1

    list = sorted(
        # 将字典的元素转化为列表，然后进行排序，降序排序，并返回前10条
        word_count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print(list)
