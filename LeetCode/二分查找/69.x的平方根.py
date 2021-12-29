num = 3000


class Solution:
    def mySqrt(self, x):
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (left + right) / 2.0
            if mid * mid <= x:
                ans = mid
                left = mid + 0.1
            else:
                right = mid - 0.1
        return ans


print(Solution().mySqrt(num))
