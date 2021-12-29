while True:
    try:
        N = int(input())
        res = []
        for i in range(N):
            if i == 0:
                res = [(e + 2)*(e + 1) // 2 for e in range(N)]
            else:
                res = [e - 1 for e in res[1:]]
            print(' '.join(map(str, res)))
    except:
        break
