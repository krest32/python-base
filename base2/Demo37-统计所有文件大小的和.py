import os
# 得到文件的大小方法，返回字节大小
print(os.path.getsize("./English.txt"))

sum_size = 0

# 获取当前目录下所有文件，同时会返回目录
for file in os.listdir("."):
    # 判断路径是不是文件
    if os.path.isfile(file):
        sum_size += os.path.getsize(file)


print("dir size {0} kb".format(sum_size/1000))