while True:
    try:
        inpt = input()
        if len(inpt) < 8:
            res = inpt + '0' * (8-len(inpt))
            print(res)
        else:
            time = int(len(inpt) // 8)
            if len(inpt) % 8 == 0:
                for i in range(time):
                    print(inpt[i*8: i*8+8])
            else:
                for i in range(time):
                    print(inpt[i*8: i*8+8])
                print(inpt[time*8:] + '0' * (8-len(inpt[time*8:])))
    except:
        break
