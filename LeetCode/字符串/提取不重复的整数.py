num = input()
res = ''
for i in range(len(num) - 1, -1, -1):
    if num[i] not in res:
        res += num[i]

print(res)
