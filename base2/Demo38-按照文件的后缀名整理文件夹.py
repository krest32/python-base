import os
# 移动文件的模块
import shutil

# 目标文件处理目录
dir = "./arrange_dir"

for file in os.listdir(dir):
    # 获取文件的后缀
    ext = os.path.splitext(file)[1]
    # 取点 .
    ext = ext[1:]
    # 如果目录不存在，那么创建文件
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")
    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"

    # 移动文件
    shutil.move(source_path,target_path)
