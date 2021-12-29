# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素

class Solution:
    def searchInsert(self, str, num):
        left, right = 0, len(str) - 1
        while left <= right:
            mid = (left + right) // 2
            if str[mid] < num:
                left = mid + 1
            elif str[mid] > num:
                right = mid - 1
            elif str[num] == num:
                return mid
        return left

        # 三行代码
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)


nums = [1, 3, 5, 6]
num = 2
print(Solution().searchInsert(nums, num))
