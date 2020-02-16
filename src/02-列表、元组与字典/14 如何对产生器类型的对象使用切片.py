from itertools import islice

gen = iter(range(10))
for x in gen:
    print(x, end=" ")
print()
print(type(gen))

# islice()
gen = iter(range(10))  # 需重新生成迭代器
for i in islice(gen, 2, 6):
    print(i)
