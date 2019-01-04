class UserInfo(object):
    lv =5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def getAccount(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self._age

class UserInfo2(UserInfo):
    def __init__(self,name, age, account,sex):
        super(UserInfo2,self).__init__(name,age,account)
        self.sex = sex


if __name__ == '__main__':
    userInfo = UserInfo('ye', 30, 242814300)
    print(dir(userInfo))
    print(userInfo.__dict__)
    print(userInfo.getAccount())
    print(userInfo._UserInfo__account)
    print("-----------------------------------------")
    print(UserInfo.lv)
    print(userInfo.get_age)
    print(UserInfo.get_age)
    print(UserInfo.get_name())
    print(userInfo.get_name())
    print("-----------------------------------------")
    userInfo2 = UserInfo2('ye2',20,222222,'mail')
    print(userInfo2.getAccount())
    print(dir(userInfo2))
    print(userInfo2.__dict__)
    print(userInfo2.get_name())
    print(userInfo2.sex)

