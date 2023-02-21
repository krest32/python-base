test_list=[1,2,3,4,5,6,7]

print("查看4是否在列表中（使用循环）：")

for i in test_list:
    if(i==4):
        print("存在")

print("查看4是否在列表中（使用in关键字）：")
if(4 in test_list):
    print("存在")