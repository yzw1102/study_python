import threading , time

class Consumer(threading.Thread):
    def __init__(self,cond,name):
        super(Consumer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ": 我这两件商品一起买，可以便宜点吗")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 我已提交订单了，你修改下价格")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 收到，我支付成功了")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 等待收货")

class Producer(threading.Thread):
    def __init__(self,cond,name):
        super(Producer,self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ": 可以，你提交订单吧")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 好了，已经修改好了")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 收款成功，发上发货")
        self.cond.release()
        print(self.name + ": 发货商品")

cond = threading.Condition()
consumer = Consumer(cond,'customer')
producer = Producer(cond,'saler')
consumer.start()
producer.start()

