while True:
    try:
        s = input()
        a = ''
        for i in s:
            if i.isalpha():
                a += i
        b = sorted(a, key=str.upper)

        index = 0
        d = ''
        for i in s:
            if i.isalpha():
                d += b[index]
                index += 1
            else:
                d += i
        print(d)
    except:
        break
