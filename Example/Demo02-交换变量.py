x = input('输入x的值：')
y = input('输入y的值：')

temp = x
x = y
y = temp

print('交换后的x的值为：{}'.format(x))
print('交换后y的值位：{}'.format(y))