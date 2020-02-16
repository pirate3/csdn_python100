# 4个区别

# 1：语法差异
a = (1, 2, 3, 4)  # 元组
b = [1, 2, 3, 4]  # 列表

# 2：元组是只读的，列表是可读写的
b[1] = 3

# 3. 元组复制不变，列表复制变
copy_a = tuple(a)
print(a is copy_a)  # True

copy_b = list(b)
print(b is copy_b)  # False

# 4：元组占用空间更小（大的内存块）
c = [{1: 2}, {2: 3}, {3: 4}, {4: 5}]  # 列表
print(a.__sizeof__())
print(b.__sizeof__())
print(c.__sizeof__())
