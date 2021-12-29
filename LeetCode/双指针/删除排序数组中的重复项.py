class Solution:
	def removeDuplicates(self, nums):
		if not nums:
			return 0

		# 初始化第一个指针i，在0的位置
		first = 0
		# 第二个指针从位置1开始
		for second in range(1, len(nums)):
			# 当两个指针所指的数值不相等时
			if nums[first] != nums[second]:
				# 第一个指针向前走一步
				first += 1
				nums[first] = nums[second]
		
		return first + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5]
print(Solution().removeDuplicates(nums))
