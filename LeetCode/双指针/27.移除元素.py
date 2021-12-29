class Solution:
	def removeElement(self, nums, val):
		left = 0
		for right in nums:
			if right != val:
				nums[left] = right
				left += 1
		return left


if __name__ == '__main__':
	nums = [3, 2, 2, 3]
	val = 3
	print(Solution().removeElement(nums, val))
