nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]


class Solution:
    def missingNumber(self, nums):
        left, right = 0, max(nums)
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left


print(Solution().missingNumber(nums))
