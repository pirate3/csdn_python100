import re

# findall()
s = '我的Email地址是abcd@163.com，你的Email是多少呢？是xyz@122.net吗？ 或者是ccc@125.org'
prefix = '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.'
result = re.findall(prefix + 'com|' + prefix + 'net', s, re.I)
print(result)

print(result[0])
print(result[1])