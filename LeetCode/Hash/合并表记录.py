n = int(input())
d = {}
for i in range(n):
    ab = input().split(' ')
    a, b = int(ab[0]), int(ab[1])
    if a not in d:
        d[a] = b
    elif a in d:
        d[a] = d[a] + b
for i in sorted(d.keys()):
    print(i, d[i])
