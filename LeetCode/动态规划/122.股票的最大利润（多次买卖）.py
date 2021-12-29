prices = [7, 1, 5, 3, 6, 4]


class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit


print(Solution().maxProfit(prices))
