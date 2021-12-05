'''
def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv

    return wrapper

@func
def func2(x, y):
    print(x)
    return y

@func
def func3():
    print("I am func3")

# func3 = func(func3)
# func3()

# func2 = func(func2)
x = func2(5, 6)
print(x)

# x = func("hello")
# print(x)
# x()

# x = func(func3)
# y = func(func2)
# print(x)
# x()
# y()
'''

import time

def timer(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time:", total)
        return rv
    
    return wrapper

@timer
def test():
    for _ in range(1000000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()