def printHello(self,name = 'py'):
    print('Hello,',name)


Hello = type('Hello',(object,),dict(hello = printHello))

h = Hello()
h.hello()
print(type(Hello))
print(type(h))