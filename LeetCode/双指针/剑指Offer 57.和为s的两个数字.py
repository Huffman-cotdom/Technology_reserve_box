class Solution():
    # def twoSum(self, nums, target):
    # 	i, j = 0, len(nums) - 1
    # 	num = []
    # 	while i < j:
    # 		s = nums[i] + nums[j]
    # 		if s > target:
    # 			j -= 1
    # 		elif s < target:
    # 			i += 1
    # 		else:
    # 			num.append((i, j))
    # 			j -= 1
    # 			i += 1

    # 	return num
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return nums[i], nums[j]


if __name__ == '__main__':
    nums, target = [1, 2, 7, 8, 11, 15], 9
    print(Solution().twoSum(nums, target))
