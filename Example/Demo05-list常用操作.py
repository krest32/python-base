
li = ["a", "b", "mpilgrim", "z", "example"]

# 从后获取元素
print(li[-1])
# 获取区间元素
print(li[1:3])
# 获取区间元素
print(li[1:-1])

# 追加元素
li.append("new")
print(li)

# 插入元素
li.insert(2, "new")
print(li)

# 批量插入元素
li.extend(["two", "elements"])
print(li)

# 搜索元素
print(li.index("example"))
# print(li.index("c"))


# list运算
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print(li)

# 扩大三倍
li = [1, 2] * 3
print(li)

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# 遍历字典
print(["%s=%s" % (k, v) for k, v in params.items()])
# 使用join链接list成为字符串
print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))


# list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)
print(s.split(";"))

# list映射
li = [1, 9, 8, 4]
li = [elem*2 for elem in li]
print(li)

# dictionary 中的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k, v in params.items()])
print([v for k, v in params.items()])
print(["%s=%s" % (k, v) for k, v in params.items()])

# list过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])