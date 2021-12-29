class Solution:
	def moveZeroes(self, nums):
		left = right = 0
		while right < len(nums):
			if nums[right] != 0:
				nums[left], nums[right] = nums[right], nums[left]
				left += 1
			right += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
