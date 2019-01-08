class User(object):

    def __getattr__(self, name):
        print('invoke __getattr__ method')
        return super(User,self).__getattr__(name)

    def __setattr__(self, name, value):
        print('invoke __setattr__ method')
        return super(User,self).__setattr__(name,value)

    def __delattr__(self, name):
        print('invoke __delattr__ method')
        return super(User,self).__delattr__(name)

    def __getattribute__(self, name):
        print('invoke __getAttribute__ method')
        return super(User,self).__getattribute__(name)


if __name__ == '__main__':
    user = User()
    user.attr1 = True
    user.attr1
    try:
        user.attr2
    except AttributeError:
        pass

    del user.attr1


