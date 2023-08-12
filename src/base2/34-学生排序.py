if __name__ == '__main__':
    students = [
        {"no": "1001", "name": "小1", "grade": 88},
        {"no": "1002", "name": "小2", "grade": 85},
        {"no": "1003", "name": "小3", "grade": 84},
        {"no": "1004", "name": "小4", "grade": 89}
    ]

    # lambda 表达式升序排列
    # students_sort = sorted(students,key=lambda  x:x["grade"])

    # 降序排列
    students_sort = sorted(students, key=lambda x: x["grade"], reverse=True)

    print(f"source {students} ")
    print(f"sort result:{students_sort}")
