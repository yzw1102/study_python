class User(object):
    def upgrade(self):
        pass
    def _buy_euqiment(self):
        pass
    def __pk(self):
        pass

class User1(object):
    pass

class User2(User1):
    pass

class User3(User2):
    pass

if __name__ == '__main__':
    user1 = User1()
    user2 = User2()
    user3 = User3()

    print(isinstance(user1,User1))
    print(isinstance(user2,User2))
    print(isinstance(user3,User3))
    print(isinstance('1adfa23',str))
    print(isinstance(12345,str))
    print(isinstance(12345,int))
