# 1.
# def print_userinfo(name,age,sex='male'):
#     print('name: {}'.format(name),end = ' | ')
#     print('age: {}'.format(age),end = ' | ')
#     print('sex: {}'.format(sex))
#     return;
# 
# print_userinfo('ye',33,'male')
# print_userinfo('cui',33,'female')
# print_userinfo('rui',6)


# 2.
# def print_userinfo(name,age,sex='male'):
#     print('name: {}'.format(name),end = ' | ')
#     print('age: {}'.format(age),end = ' | ')
#     print('sex: {}'.format(sex))
#     return;
# 
# print_userinfo(name = 'ye',age=20,sex = 'male')
# print_userinfo(name = 'ye',sex = 'male',age=30)


# 3.
# def print_userinfo(name,age,sex='male',*hobby):
#     print('name: {}'.format(name),end = ' | ')
#     print('age: {}'.format(age),end = ' | ')
#     print('sex: {}'.format(sex),end = ' | ')
#     print('hobby: {}'.format(hobby))
#     return;
# 
# print_userinfo('ye',20,'male','game','swimming')

# 4.
# def print_userinfo(name,age,sex='male',**hobby):
#     print('name: {}'.format(name),end = ' | ')
#     print('age: {}'.format(age),end = ' | ')
#     print('sex: {}'.format(sex),end = ' | ')
#     print('hobby: {}'.format(hobby))
#     return;
# 
# print_userinfo(name='ye',age=20,sex='male',hobby=('game','swimming'))

# 5.
def print_userinfo(name,*,age,sex='male'):
    print('name: {}'.format(name),end = ' | ')
    print('age: {}'.format(age),end = ' | ')
    print('sex: {}'.format(sex),)
    return;

print_userinfo('ye',age=20,sex='male')


