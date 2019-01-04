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



if __name__ == '__main__':
    userInfo = UserInfo('ye', 30, 242814300)
    print(dir(userInfo))
    print(userInfo.__dict__)
    print(userInfo.getAccount())
    print(userInfo._UserInfo__account)

    print(UserInfo.lv)
    print(userInfo.get_age)
    print(UserInfo.get_age)
    print(UserInfo.get_name())
    print(userInfo.get_name())

