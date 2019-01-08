from enum import Enum

class User(Enum):
    Ye = 100
    Cui = 90
    Tom = 10

Ye = User.Ye
Cui = User.Cui

print(Ye == Cui)
print(Ye == User.Ye)

print(Ye is Cui)
print(Ye is User.Ye)


