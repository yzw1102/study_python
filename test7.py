# 1.
# count = 1
# sum = 0
# while (count <= 100):
#     sum = sum + count
#     count = count + 1
# print(sum)

# 2.
# count = 1
# sum = 0
# while (count <= 100):
#     sum += count
#     if(sum > 1000):
#         break
#     count += 1
# print(sum)

# 3.
count = 1
sum = 0
while count <= 100:
    if count % 2 == 0:
        count += 1
        continue
    sum += count
    count += 1
print(sum)

# 4.
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('越界了',count)

# 5.
# for l in 'hello world':
#     if l == 'o':
#         break;
#     print(l)
# else:
#     print('else...')

