# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标。

class Solution:
    def canJump(self, nums) -> bool:
        # 跳跃最大距离
        max_distence = 0
        for distence, jump in enumerate(nums):
            if max_distence >= distence and distence + jump > max_distence:
                # 如果能够到达当前位置，并且当前位置 + 跳跃距离 > 当前跳跃的最大距离，就接着跳到下一个位置，记录下跳跃的最大距离
                max_distence = distence + jump

        # 如果跳跃的最大距离大于总距离，返回True
        return max_distence > distence


nums = [2, 3, 0, 1, 4]
print(Solution().canJump(nums))
