# 1. 通过索引获取字符串中的某个字符
s1 = 'hello world'
print(s1[0])
print(s1[2])

# 2. 分片
print(s1[6:9])
print(s1[6:])
print(s1[::2])
print(s1[::-1])  # 指定步长

s2 = "xyz"
print(10 * s2)  # 翻倍
print(s2 * 20)

print('b' in s2)  # 判断是否包含某个字符
print('y' in s2)
print('b' not in s2)

print(len(s1))  # 长度
print(min(s2))  # 最小字符
print(max(s2))  # 最大字符

# 列表
a = [1, 2, 3, 0, 6]
print(2 not in a)

print(max(a))
print(min(a))
print(len(a))

print(10 * a)  # 翻倍

a[0] = 20
