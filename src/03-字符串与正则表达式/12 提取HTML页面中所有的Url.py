import re

s = '<a href="https://geekori.com">极客起源</a> <a href="https://www.microsoft.com">微软</a>'

# findall() re.I忽略大小写
result = re.findall('<a[^>]*href="([^>]*)">', s, re.I)
print(result)
for url in result:
    print(url)
