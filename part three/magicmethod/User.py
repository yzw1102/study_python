class User(object):
    def __new__(cls, *args, **kwargs):
        print("invoke __new__ method.")
        print(args)
        return super(User, cls).__new__(cls)

    def __init__(self,name,age):
        print('invoke __init__ method.')
        self.name = name
        self.age = age


if __name__ == '__main__':
    user = User('ye',33)
