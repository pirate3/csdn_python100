a = [i for i in range(10)]  # 使用方括号，这个是列表
print(a)
print(type(a))  # <class 'list'>

b = (i for i in range(10))  # 使用圆括号，这个是产生器
print(b)
print(type(b))  # <class 'generator'>

for i in a:
    print(i)

for i in b:
    print(i * i)

x = (1, 2, 3, 4)  # 这样定义的是元组
print(type(x))  # <class 'tuple'>
