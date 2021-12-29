while True:
    try:
        total_money, total_num = map(int, input().split(' '))
        total_money //= 10
        product_item = []
        for i in range(total_num):
            v, p, q = map(int, input().split(' '))
            v //= 10
            product_item += [[i+1, v, p, q]]
        dp = [[0, [0]] for i in range(total_money+1)]

        for current_no, v, p, q in product_item:
            for i in range(len(dp)-1, -1, -1):
                if (i-v) >= 0:
                    if not current_no in dp[i-v][1]:
                        if q in dp[i-v][1]:  # the parent has been chosen.
                            if (dp[i-v][0]+v*p) > dp[i][0]:
                                dp[i][0] = dp[i-v][0]+v*p
                                dp[i][1] = dp[i-v][1].copy()
                                dp[i][1] += [current_no]
                        else:  # the parent has not been chosen, then we can pick up both current one and the parent.
                            if (i-v-product_item[q-1][1]) > 0:
                                if (dp[i-v-product_item[q-1][1]][0]+v*p+product_item[q-1][1]*product_item[q-1][2]) > dp[i][0] and not current_no in dp[i-v-product_item[q-1][1]][1] and not q in dp[i-v-product_item[q-1][1]][1]:
                                    dp[i][0] = dp[i-v-product_item[q-1][1]][0] + \
                                        v*p+product_item[q-1][1] * \
                                        product_item[q-1][2]
                                    dp[i][1] = dp[i-v-product_item[q-1][1]][1].copy()
                                    dp[i][1] += [current_no]
                                    dp[i][1] += [q]
        print(dp[total_money][0]*10)
    except:
        break
