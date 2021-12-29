# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

class Solution:
    def jump(self, nums) -> int:
    	total_step, max_jump, next_start = 0, 0, 0
    	for i in range(len(nums) - 1):
    		# 寻找当前位置能跳距离之内的存在最大值的点，作为下一次跳跃点
    		max_jump = max(max_jump, i + nums[i])	

    		if i == next_start:
    			next_start = max_jump
    			total_step += 1

    	return total_step


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
