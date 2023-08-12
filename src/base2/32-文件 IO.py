if __name__ == '__main__':
    # 写文件
    with open("test.txt", "wt") as out_file:
        out_file.write("写入文件\n看到我了吧 ")
    # 读文件
    with open("test.txt", "rt") as in_file:
        text = in_file.read()

    print(text)
