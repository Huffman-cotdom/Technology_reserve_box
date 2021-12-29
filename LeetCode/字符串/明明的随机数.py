while True:
    try:
        count = int(input())
        numbers1 = [int(input()) for x in range(count)]
        result1 = sorted(set(numbers1))

        for i in result1:
            print(i)

    except:
        break
