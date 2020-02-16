def oneNumber(n):
    print(bin(n))
    # 符号数在内存由补码表示
    # 若为负数，此处需要去符号位，即把负值的表示转为正值的表示
    # 否则后续&运算时程序会先做补位运算再做&运算，结果是原码的&运算
    # 原码、反码、补码，参考https://wenku.baidu.com/view/cb9f8af80b1c59eef9c7b44b.html
    if n < 0:
        n = n & 0xffffffff
    print(bin(n))
    m = len(bin(n)) - 2  # 前2位是二进制标识符
    count = 0
    '''
    1101 = 13
    0001   = 1 count++
    0000   = 0 
    0100   = 4 count++
    1000   = 8 count++
    '''
    for i in range(0, m):
        if n & 2 ** i != 0:  # &按位与运算
            count += 1
    return count


print(oneNumber(13))
print("=" * 30)
print(oneNumber(-1))
print("=" * 30)
print(oneNumber(-2))
