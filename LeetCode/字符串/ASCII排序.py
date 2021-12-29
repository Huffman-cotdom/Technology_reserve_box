while True:
    try:
        arr = sorted(input())
        sorted_arr = ''
        for i in arr:
            sorted_arr += i
        print(sorted_arr)

    except:
        break
