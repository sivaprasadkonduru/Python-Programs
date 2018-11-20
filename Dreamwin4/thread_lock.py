import threading
import time
from threading import Lock

total = 0
lock = Lock()


def count_var():
    #try:
    #lock.acquire()
    with lock:
        global total
        total += 1
        time.sleep(2)
        print(total)
        print('hello')
        #finally:
        print('Done')
        #lock.release()


for i in range(5):
    #import pdb; pdb.set_trace()
    t = threading.Thread(target=count_var)
    t.start()
    #time.sleep(3)


#for i in range(5):
#    print(i*i)



