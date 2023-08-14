if __name__ == '__main__':
    like_count = {}
    with open("42-text.txt", "r", encoding="utf-8-sig") as fin:
        for line in fin:
            line = line[:-1]
            name, likes = line.split(" ")
            like_list = likes.split(",")
            for like in like_list:
                if like not in like_count:
                    like_count[like] = 0
                like_count[like] += 1

    # 统计每个兴趣爱好的人数
    print(like_count)
