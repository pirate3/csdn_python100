'''
q1
with语句适用于对资源进行访问的场合，可确保不管使用过程是否发生异常都会执行必要的"清理"或“关闭”工作
'''

f = open('files/readme.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()

'''
1. 没有关闭文件
2. 即使关闭了文件，但在关闭之前如果抛出异常，仍然会无法关闭文件
'''

f = open('files/readme.txt', 'r', encoding='utf-8')
try:
    data = f.read()
except:
    print('抛出异常')
finally:
    f.close()

with open('files/readme.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)

'''
q2
将with语句用于自定义的类
必须定义__enter__、__exit__
'''


class MyCass:
    def __enter__(self):
        print('__enter__() is call!')
        return self

    def process1(self):
        print('process1')

    def process2(self):
        x = 1 / 0
        print('process2')

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__() is call!')
        print(f'type:{exc_type}')
        print(f'value:{exc_value}')
        print(f'trace:{traceback}')

print("------------")
with MyCass() as my:
    my.process1()
    my.process2()
