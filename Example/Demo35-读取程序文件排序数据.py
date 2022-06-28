# 按行读取文件的内容
def read_file():
    result = []
    # 使用utf-8的方式打开文件
    with open("./student_grade_input.txt",'r',encoding='utf-8-sig') as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result

def sort_list(datas):
    # 按照列表中的第三个元素进行排序
    return sorted(datas,key=lambda x: int(x[2]),reverse=True)

def write_file(datas):
    with open("./student_grade_output.txt","w",encoding='utf-8-sig') as fout:
        for data in datas:
            # 将数据写入到文件中，，为分隔符，最后再加上一个换行符
            fout.write(",".join(data)+"\n")
    print("文件写出成功")




# 读取文件
datas = read_file()
print("read file datas:",datas)

# 排序数据
datas = sort_list(datas)
print("sorted datas:",datas)

# 写出文件
write_file(datas)