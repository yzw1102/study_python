from queue import Queue
from threading import Thread
import time

isRead = True

def write(q):
    for value in ['ye1','ye2','ye3']:
        print('the value write in queue is : {0} '.format(value))
        q.put(value)
        time.sleep(1)

def read(q):
    while isRead:
        value = q.get(True)
        print('the value get from queue is : {0}'.format(value))

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target = write,args = (q,))
    t2 = Thread(target = read, args = (q,))
    t1.start()
    t2.start()