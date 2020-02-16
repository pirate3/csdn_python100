# q1
'''
装饰器是一个函数
面向切面
参考https://www.jianshu.com/p/ee82b941772a
'''

from functools import wraps


def log(flag):
    def decorate(func):
        @wraps(func)
        def _wrap(*args, **kwargs):
            try:
                if flag:
                    func(*args, **kwargs)
                print('name', func.__name__)
            except Exception as e:
                print(e.args)

        return _wrap

    return decorate


@log(True)
def add(a, b, c):
    print('sum', '=', a + b + c)


add(1, 2, 3)
