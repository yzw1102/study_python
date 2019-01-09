class Test(object):
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
