import threading
import time

time1 = time.time()
def hello(n):
    print('hello' * n)


def welcome(n):
    #time.sleep(2)
    print('welcome to python' * n)


if __name__ == '__main__':
    hello(3)
    welcome(2)
    time2 = time.time()
    timediff = time2 - time1
    print(timediff)
