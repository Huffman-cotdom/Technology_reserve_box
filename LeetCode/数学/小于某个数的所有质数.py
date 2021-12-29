def fun(n):
    list1 = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:  # 这里的else承接的是for循环里的条件判断
            list1.append(i)
    return list1


n = int(input('输入一个数：'))
print(fun(n))
