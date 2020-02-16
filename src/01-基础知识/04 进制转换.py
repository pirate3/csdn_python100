# 第一题：二进制、八进制和十六进制的表示方法
n1 = 1234
# 二进制 0B
n2 = 0B11101

print(n2)
# 八进制 0O
n3 = 0O127
print(n3)

# 十六进制 0X
n4 = 0XF15
print(n4)

print("---------------------------")

# 进制之间的转换
# 八进制转换为二进制 bin()
print(bin(0O3))

# 十进制转换为二进制 bin()
print(bin(120))

# 十六进制转换为二进制 bin()
print(bin(0xF012A))

# 二进制转为八进制 oct()
print("二进制转为八进制", oct(0B11))

# 十进制转为八进制 oct()
print(oct(1234))

# 十六进制转为八进制 oct()
print("十六进制转为八进制", oct(0xF012A))

# 将二进制转为十进制 int()
print("将二进制转为十进制", int(0B10110))
print(int('10110', 2))

# 将八进制转为十进制 int()
print(int('3213', 8))

# 十六进制转十进制 int()
print(int('0XF35AE', 16))
print(int('F35AE', 16))

# 将二进制转换为十六进制 hex()
print(hex(0b1101110101))

# 将八进制转为十六进制 hex()
print("将八进制转为十六进制", hex(0B11101))

# 十进制转为十六进制 hex()
print(hex(54321))

# 输出仍然是十进制
print(0b11010101 * 0XF12 * 0o432 * 123)
