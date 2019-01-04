# 1.
# list1 = [x*x for x in range(1,10)]
# print(list1)
# list2 = [x*x for x in range(1,10) if x %2 == 0]
# print(list2)

# 2.
# gen = (x * x for x in range(1,10))
# print(gen)
# for num in gen:
#     print(num)

# 3.
# gen = (x * x for x in range(1,10))
# print(gen)
# iter1 = iter(gen)
# for num in range(2):
#     print(next(iter1))

# 4.
# def my_function():
#     for i in range(10):
#         print(i)
# 
# my_function()

# 5. 没有想明白，回来再看一下
# def my_function():
#     for i in range(10):
#         yield i 
# 
# f = my_function()        
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


# 6.
# def odd():
#     print('step 1')
#     yield(1)
#     print('step 2')
#     yield(2)
#     print('step 3')
#     yield(3)
# 
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))

# 7. 
def fibon(n):
    a = b =1
    for i in range(n):
        yield a 
        a,b = b,a+b

for x in fibon(10):
    print(x,end = '')




