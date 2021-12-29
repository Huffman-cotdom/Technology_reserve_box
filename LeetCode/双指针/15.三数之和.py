# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # c对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举b
            for second in range(first + 1, n):
                # 需要和上次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                # 需要保证b的指针在c的指针左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着b后续的增加，就不会有满足a + b + c = 0 并且 b < c,退出循环
                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
