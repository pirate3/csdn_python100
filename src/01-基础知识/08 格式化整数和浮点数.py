# 格式化整数和浮点数

# 题目1：格式化整数 d指定宽度 >左侧补 <右侧补
n = 1234
print(format(n, '10d'))     # 右对齐
print(format(n, '0>10d'))
print(format(n, '0<10d'))

# 题目2：格式化浮点数
x1 = 1234.56789
x2 = 30.1
print(format(x1, '0.2f'))  # 保留小数点后两位
print(format(x2, '0.2f'))

# 题目3：描述format函数
print(format(x2, '*>15.4f'))  # 右对齐，********30.1000
print(format(x2, '*<15.4f'))  # 左对齐，30.1000********
print(format(x2, '*^15.4f'))  # 中心对齐，****30.1000****
print(format(123456789, ','))  # 用千位号分隔，123,456,789
print(format(1234567.865565656, ',.2f'))  # 1,234,567.87

print(format(x1, 'E'))
print(format(x1, '0.2E'))
