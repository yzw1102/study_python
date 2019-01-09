age = 23
print(age.__class__)

name = 'ye'
print(name.__class__)

def fu():
    pass
print(fu.__class__)

class eat(object):
    pass

mEat = eat()

print(mEat.__class__)

print(age.__class__.__class__)
print(name.__class__.__class__)
print(fu.__class__.__class__)
print(mEat.__class__.__class__)

