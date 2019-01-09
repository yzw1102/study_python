import threading

class mThread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)

    def run(self):
        global event

        if event.isSet():
            event.clear()
            event.wait()
            print(self.getName() + '--true')
        else:
            print(self.getName() + '--false')
            event.set()

event = threading.Event()
event.set()
t1 = []
for i in range(10):
    t = mThread('thread-' + str(i))
    t1.append(t)

for i in t1:
    i.start()