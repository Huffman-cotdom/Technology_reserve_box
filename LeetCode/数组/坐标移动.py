while True:
    try:
        string = input().strip().split(';')
        start = [0, 0]
        for i in string:
            if not i:
                continue
            try:
                if i[0] == 'A':
                    start[0] -= int(float(i[1:]))
                if i[0] == 'D':
                    start[0] += int(float(i[1:]))
                if i[0] == 'S':
                    start[1] -= int(float(i[1:]))
                if i[0] == 'W':
                    start[1] += int(float(i[1:]))
            except:
                continue
        print('%d,%d' % (start[0], start[1]))
    except:
        break
