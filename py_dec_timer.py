from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('Elapsed: ', after - before)
        return rv

    return f


@timer
def add(x, y=10):
    return x + y


@timer
def sub(x, y=10):
    return x - y


print('add(10)', add(15))
print('sub(20,30)', sub(20, 30))
