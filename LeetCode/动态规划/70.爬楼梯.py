n = 11


class Solution:
    def climbStair(self, n):
        if n <= 2:
            return n
        stair1 = 1
        stair2 = 2
        cur = 0
        for i in range(2, n):
            cur = stair1 + stair2
            stair1 = stair2
            stair2 = cur
        return cur


print(Solution().climbStair(n))
