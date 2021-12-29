class Solution:
    def rob(self, nums):
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        # pre1 = pre2 = 0
        # for i in range(n):
        #     cur = max(pre2 + nums[i], pre1)
        #     pre2 = pre1
        #     pre1 = cur
        # return cur

        prev, curr = 0, 0
        for i in nums:
            prev, curr = curr, max(curr, prev + i)
        return curr


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
