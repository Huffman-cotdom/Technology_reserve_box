prices = [7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices):
        # 两次遍历
        # ans = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         ans = max(ans, prices[j] - prices[i])
        # return ans

        # 一次遍历
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


print(Solution().maxProfit(prices))
