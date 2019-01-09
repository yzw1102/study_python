import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number:{}'.format(self.name,i))
            time.sleep(1)

def main():
    print('start main thread')

    threads = [MyThread() for i in range(3)]

    print(threads)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('end main thread')

if __name__ == '__main__':
    main()

