# 列表和字典 不可作为字典的key，因为它们是可变的

d = {}
d['name'] = 'Bill'
d[10] = 20
d[True] = False
d[12.3] = 20.1

d[(1, 2, 3)] = [4, 5, 6]  # 元组可以作为key


class Person:
    pass


p1 = Person()
p2 = Person()

d[p1] = "p1"  # 对象可以作为key
d[p2] = 'p2'

print(d)
print(d[12.3])

# d[[1,2,3]] = 3
# d[{'a:',3}] = 4

# 因为key是不能变的。但列表和字典的值是可以变化的，一旦变化，就再也找不到对应的value了
