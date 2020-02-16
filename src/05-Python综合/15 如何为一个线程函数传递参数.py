import threading


# 线程函数
def func1(fun, s):
    print('正在执行函数func1')
    fun(s)


def ff(s):
    print(f'ff输出了{s}')

# 在线程中执行带参数的函数
t1 = threading.Thread(target=func1, args=(ff, "hello world"))
t1.start()
