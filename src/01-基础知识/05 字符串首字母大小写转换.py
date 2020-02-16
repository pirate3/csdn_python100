# 字符串首字母大小写转换

# 第一题：首字母转大写 capitalize()
s1 = 'hello'
print(s1)
print(s1.capitalize())

# s1[0] = 'H'  只读的，会抛出异常
s1 = s1[0].upper() + s1[1:]
print(s1)

s2 = 'Hello'
s = s2[0].lower() + s2[1:]
print(s)

# 第二题：如何将字符串中每一个单词的首字母变成大写
s3 = 'hello world'
print(s3.capitalize())

arr = s3.split(' ')
print(arr)
new_str = f'{arr[0].capitalize()} {arr[1].capitalize()}'
print("如何将字符串中每一个单词的首字母变成大写:", new_str, sep="")

new_str2 = ' '.join([x.capitalize() for x in arr])
print("如何将字符串中每一个单词的首字母变成大写2:", new_str2)

new_str3 = f'{[x.capitalize() for x in arr]}'
print("如何将字符串中每一个单词的首字母变成大写3:", new_str3)