def upper_attr(future_class_name,future_class_parents,future_class_attr):

    attrs = ((name,value) for name,value in future_class_attr.itmes() if not name.startswith('__'))

    print('attr------',attrs)

    uppercase_attr = dict((name.upper(),value) for name,value in attrs)

    return type(future_class_name,future_class_parents,uppercase_attr)

__metaclass__ = upper_attr
class Foo(object):
    bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f = Foo()
print(f.bar)
# print(f.BAR)
print(Foo.__dict__)
print(Foo.__class__)
