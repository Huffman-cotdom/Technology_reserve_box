while True:
    try:
        num = int(input())
        name = []
        for i in range(num):
            name.append(input())
        res = [0] * num
        for i in range(num):
            temp = set(list(name[i]))
            d = []
            for j in temp:
                d.append(name[i].count(j))
                d.sort(reverse=True)
            for k in range(len(d)):
                res[i] = res[i] + d[k] * (26 - k)
        for i in range(num):
            print(res[i])

    except:
        break
