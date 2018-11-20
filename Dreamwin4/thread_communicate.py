import threading
from multiprocessing import Queue
import queue

items = ['car', 'two-wheeler', 'plane']

def execute():
    if q.not_empty:
        print('In execute method')
        item = q.get()
        val = item * 2
        print(val)
        q.task_done()
        #print(q.get())

q = queue.Queue()
tlist = []
for i in range(4):
    t = threading.Thread(target=execute)
    tlist.append(t)
    t.start()

for item in items:
    q.put(item)  # put the items in queue

#for i in tlist:
#    i.join()

q.join()

print('done')
print('exit')
#q.join()
#print(q.unfinished_tasks)