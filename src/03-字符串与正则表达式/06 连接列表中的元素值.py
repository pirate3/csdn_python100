'''
q1
'''
# join()
a = ['a', 'b', 'c', 'd', 'e']
s = "+"
print(s.join(a))

'''
q2
'''

# 拼接路径
dirs = '', 'usr', 'local', 'nginx', ''  # 定义元组
print(dirs)
linuxPath = '/'.join(dirs)
print(linuxPath)

windowPath = 'C:' + '\\'.join(dirs)
print(windowPath)

# 不可连接数字
num = [1, 2, 3, 4, 5]
print(s.join(num))
