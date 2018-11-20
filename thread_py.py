import threading
import time

time1 = time.time()
def hello(n):
    print('hello' * n)


def welcome(n):
    time.sleep(1)
    print('welcome to python' * n)


t = threading.Thread(target=welcome, args=(2, ))
t1 = threading.Thread(target=welcome, args=(3, ))

t.start()   # run()
t1.start()  # run()

#t.join()  # it will wait till thread1 completes the target
#t1.join() # it will wait till thread2 completes the target
time2 = time.time()
timediff = time2 - time1
print(timediff)
print('hello python')
