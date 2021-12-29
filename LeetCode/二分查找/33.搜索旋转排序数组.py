class Solution:
    def search(self, nums, target):
        if len(nums) <= 0:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            # 如果中间的值大于最右边的值，说明左边有序
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    # 这里加1是因为上面的 <= 符号
                    left = mid + 1
            else:
                # mid + 1
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid


        return left if nums[left] == target else -1


nums = [4,5,6,7,0,1,2]
target = 5
print(Solution().search(nums, target))
