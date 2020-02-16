'''
threading.local
参考https://www.jianshu.com/p/a4aedd66af7c
'''

import threading
import time

# 针对当前线程，不可在多个线程之间共享
a = threading.local()


# 定义线程函数
def worker(b):
    a.x = 0
    for i in range(5):
        time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(), a.x)


for i in range(10):
    threading.Thread(target=worker).start()
