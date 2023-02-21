def main():
    # i 从1-10开始循环  i>=1 && i<10
    for i in range(1,10):
        # j从 1-i 开始循环 j>=1 && j<i
        for j in range(1,i+1):
            # format 传递进入的参数,\t 制表符 end 连接空格
            print('\t {0}X{1}={2}\t'.format(j, i, i*j), end=' | ')
        print()

if __name__ == "__main__":
    main()