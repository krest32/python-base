course_teacher_map = {}
with open("Demo40-txt", "r", encoding="utf-8-sig") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_map[course]=teacher

# 打印获取的文件信息
print(course_teacher_map)

def write_file(datas):
    with open("./Demo40-result.txt","w",encoding='utf-8-sig') as fout:
        # 将数据写入到文件中，，为分隔符，最后再加上一个换行符
        for data in datas:
            fout.write(",".join(data)+"\n")
    print("文件写出成功")

datas = []

# 获取文件关联的信息
with open("./Demo39-txt", "r", encoding="utf-8-sig") as fin:
    for line in fin:
        line = line[:-1]
        course, no, grade = line.split(",")
        teacher = course_teacher_map.get(course)
        list = [course, teacher, no, grade]
        # 将 list 加入到 data 中
        datas.append(list)
print(datas)
# 写出文件
write_file(datas)


