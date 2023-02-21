# 使用字段处理信息
# keys = course value = grade List
course_grades = {}
with open("Demo39-txt","r",encoding="utf-8-sig")as fin:
    for line in fin:
        line = line[:-1]
        # 将每行的信息拆分成列表
        course,no,grade = line.split(",")

        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))

print(course_grades)

# 遍历当前的成绩列表
for course, grade in course_grades.items():
    # 打印 最高分 最低 平均
    print(
        course,
        max(grade),
        min(grade),
        sum(grade)/len(grade),
    )