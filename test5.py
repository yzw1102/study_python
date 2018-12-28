# 1.
# list1 = [1,2,3,4,5]
# print('list  : ', list1)
# tuple1 = 1,2,3,4,5
# print('tuple : ',tuple1)
# set1 = set([1,2,3,4,5])
# print('set   : ',set1)

# 2.
# set1 = set([123,456,789])
# print(set1)
# set1.add(100)
# print(set1)
# set1.add(100)
# print(set1)
# set1.remove(123)
# print(set1)

# 3.
set1 = set('hello')
set2 = set(['p','y','t','h','o','n'])
print('set1 : ',set1)
print('set2 : ',set2)
set3 = set1 & set2
print('set1-set2-交集 : ',set3)
set4 = set1 | set2
print('set1-set2-并集 : ',set4)
set5 = set1 - set2
set6 = set2 - set1
print('set1-set2-差集 : ',set5)
print('set2-set1-差集 : ',set6)

