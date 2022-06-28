import os

data_dir = "./Demo41-test"

contents = []

for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8-sig") as fin:
            contents.append(fin.read())
# 在每个文件的内容中追加一个换行符
final_content = "\n".join(contents)

with open("./Demo41-test/result.txt","w",encoding="utf-8-sig") as fout:
    fout.write(final_content)