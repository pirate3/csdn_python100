class MyClass:
    def __init__(self):
        self.value = 0

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


my1 = MyClass()
my1.value = 20

my2 = MyClass()
my2.value = 10

my3 = MyClass()
my3.value = 30

a = [my1, my2, my3]
x = [my1, my2, my3]
print(a)

import operator

# 第一题： sort()
# 1.使用key=operator.attrgetter('value')
# 2.定义__gt__或__lt__，优先使用___lt__
# 3.使用lambda表达式
a.sort(key=operator.attrgetter('value'))
b = sorted(x, key=operator.attrgetter('value'))
c = sorted(x, key=lambda x:x.value)

print(a[0].value)
print(a[1].value)
print(a[2].value)

print()
print(b[0].value)
print(b[1].value)
print(b[2].value)

print()
print(c[0].value)
print(c[1].value)
print(c[2].value)

print("----------------------------")

# 第二题：降序排序
# 1.reverse=True
# 2.__gt__或__lt__反定义，优先使用___lt__
a.sort(reverse=True)
print(a[0].value)
print(a[1].value)
print(a[2].value)
