class User(object):
    def __init__(self,name):
        self.name = name

    def printUser(self):
        print('Hello' + self.name)

class UserVip(User):
    def printUser(self):
        print('Hello vip:' + self.name)

class UserGeneral(User):
    def printUser(self):
        print('Hello general:' + self.name)

def printUserInfo(user):
    user.printUser()

if __name__ == '__main__':
    userVip = UserVip('vip')
    printUserInfo(userVip)
    usergeneral = UserGeneral('general')
    printUserInfo(usergeneral)

