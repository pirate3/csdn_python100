import numpy as np
from datetime import datetime


# 获取第n个丑数，n从1开始
# 返回：目标丑数，丑数列表
# 丑数：只包含质因子2，3和5的数称作丑数（Ugly Number），1为最小丑数
# 核心思想：新丑数一定是由已得丑数乘丑数因子得到的，要得到有序丑数列表，在已得丑数列表基础上依次追加未得最小丑数即可，进而可得第n个丑数
#
def getUglyNumber(n):
    if n < 1:
        return 0, []

    # 入参为序号，转为索引
    index = n - 1

    # 定义丑数列表并初始化前3个，3以后的丑数由程序有序添加
    ugly = [1, 2, 3]
    if index < 3:
        return ugly[index], ugly

    '''
    定义并初始化最小预备丑数二维数组
    数组每行分别为2、3、5对应最小预备丑数 和 计算最小预备丑数时使用的丑数列表中丑数的索引
    最小预备丑数=丑数因子*丑数列表中该丑数因子未乘的最小丑数  
    '''
    ugly_factor = [2, 3, 5]  # 丑数因子
    pro_ugly = np.array([[ugly_factor[0] * ugly[1], 1],  # 2已加入丑数列表，此处放2*2=4
                         [ugly_factor[1] * ugly[1], 1],  # 3已加入丑数列表，此处放3*2=6
                         [ugly_factor[2] * ugly[0], 0]])  # 此处放5*1=5

    # 向丑数列表中有序追加丑数，直到丑数数量达到要获取的序号（入参）
    while (True):

        # 从最小预备丑数二维数组中获取最小预备丑数、丑数列表索引和丑数因子索引
        ugly_factor_index = np.argmin(pro_ugly[:, 0])  # 丑数因子索引
        min_pro_ugly, ugly_index = pro_ugly[ugly_factor_index]  # 最小预备丑数、丑数列表索引

        # 将获取到的最小预备丑数追加到丑数列表
        # 注意，因为获取到的最小预备丑数一定大于丑数列表中的丑数，所以该追加是自然有序的
        ugly.append(min_pro_ugly)

        # 若找到第index个丑数，返回该丑数和丑数列表
        if (len(ugly) > index):
            return ugly[index], ugly

        # 更新取走的最小预备丑数
        while (True):

            # 计算新的最小预备丑数，丑数因子*丑数列表中该丑数因子未乘的最小丑数
            ugly_index += 1
            new_pro_ugly = ugly_factor[ugly_factor_index] * ugly[ugly_index]

            # 更新取走的最小预备丑数，新最小预备丑数不可以与已存在的最小预备丑数重复
            if (new_pro_ugly not in pro_ugly[:, 0]):
                pro_ugly[ugly_factor_index] = [new_pro_ugly, ugly_index]
                break


# 测试
begin = datetime.now()
uglyNum, ugly = getUglyNumber(5)
end = datetime.now()
print("uglyNum", uglyNum)
print("uglyNum", ugly)
print("time consuming(microseconds)", (end - begin).microseconds)
