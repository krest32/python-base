total1 = 0
total2 = 0
total3 = 0
lst1 = [1, 2, 3]

# 使用循环
for ele in range(0, len(lst1)):
    total1 = total1 + lst1[ele]
print("元素之和：", total1)

# 使用while
ele = 0
while (ele < len(lst1)):
    total2 = total2 + lst1[ele]
    ele += 1

print("元素之和：", total2)


# 使用递归
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


if __name__ == '__main__':
    total3 = sumOfList(lst1, len(lst1))
    print("元素之和：", total3)
