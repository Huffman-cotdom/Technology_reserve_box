# num = input()
# res = ''
# count = 0
# for i in num:
#     if i in res:
#         continue
#     else:
#         res += i
#         count += 1

# print(count)

# Hash
num = input()
res = {}
for i in num:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

print(len(res))
