# 清空列表
lst = [1, 3, 2, 5, 6]
print("清空前：",lst)

lst.clear()
print("清空后：",lst)


# 复制列表，从0开始拷贝
def clone_lst(lst1):
    lst_copy = lst1[:]
    return lst_copy

li1 = [1,2,3]
li2 = clone_lst(li1)
print("原始列表:",li1)
print("克隆列表：",li2)

# 计算元素在列表中出现的次数
def countX(lst, x):
    count = 0
    for ele in lst:
        if(ele == x):
            count = count+1
    return  count

lst=[2,2,3,4,5,6,7,7,6,5,5,4]
x=2
print(countX(lst,x))

# 计算元素在列表中出现的次数
print(lst.count(3))






