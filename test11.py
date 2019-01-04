# 1. 
# for char in 'iterator':
#     print(char,end = ' | ')

# 2.
# list1 = [1,2,3,4,5]
# for num in list1:
#     print(num,end = ' | ')

# 3.
# dict1 = {'name':'ye','age':20}
# for key in dict1:
#     print(key,end = ' | ')
# 
# for value in dict1.values():
#     print(value,end = ' | ')

# 4.
# list1 = [(1,'a'),(2,'b'),(3,'c')]
# for x,y in list1:
#     print(x,y)

# 5. 
# str1 = 'iterator'
# iter1 = iter(str1)
# for x in iter1:
#     print(x)

# 6.
str1 = 'iterator'
iter1 = iter(str1)
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break
