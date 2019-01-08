class User(object):
    def __init__(self,name='ye',sex='male'):
        self.name = name
        self.sex = sex

    def __get__(self, instance, owner):
        print('get name value')
        return self.name

    def __set__(self, instance, value):
        print('set name value')
        self.name = value

class MyClass(object):
    x = User('ye','male')
    y = 5

if __name__ == '__main__':
    m = MyClass()
    print(m.x)
    print('\n')
    m.x = 'aa'
    print(m.x)
    print('\n')
    print(m.y)

