while True:
    try:
        high = int(input())
        sm = high
        for i in range(4):
            high /= 2
            sm += 2 * high
        high /= 2
        print(sm)
        print("%.5f" % high)
    except:
        break
