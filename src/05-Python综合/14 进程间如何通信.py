'''
参考https://www.jianshu.com/p/5009ff36ee7f/
'''
from multiprocessing import Queue, Process
import time, random

list1 = ["1-java", "2-Python", "3-JavaScript"]


def write(queue):
    for value in list1:
        print(f"正在向队列中添加数据-->{value}")
        queue.put_nowait(value)
        time.sleep(random.random())


def read(queue):
    while True:
        if not queue.empty():
            value = queue.get_nowait()
            print(f"从队列中读取的数据为-->{value}")
            time.sleep(random.random())
        else:
            break


# Process()
if __name__ == "__main__":
    queue = Queue()
    write_data = Process(target=write, args=(queue,))
    read_data = Process(target=read, args=(queue,))

    write_data.start()
    write_data.join()
    read_data.start()
    read_data.join()
    print('ok')
