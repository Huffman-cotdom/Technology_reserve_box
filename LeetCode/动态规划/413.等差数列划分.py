"""
    nums = [1,2,3,4,5,6,12,14,16]
    diffs = [1,1,1,1,1,6,2,2]
    cons = [5,1,2]
    # 将 1 舍去，nums 中有长度为 5+1 和 2+1 的等差数列
    result = (6-2)(6-1)/2 + (3-2)(3-1)/2
"""
nums = [1, 2, 3, 4, 5, 6, 12, 14, 16]


class Solution:
    def numberOfArithmeticSlices(self, nums):
        # 计算数列的差值
        diffs = []
        for i in range(len(nums) - 1):
            diffs.append(nums[i + 1] - nums[i])

        # 计算其中连续相同的差值的数目
        cons = []
        a = 1
        for i in range(1, len(diffs)):
            if diffs[i] == diffs[i - 1]:
                a += 1
            else:
                cons.append(a)
                a = 1
        cons.append(a)

        res = 0
        for num in cons:
            res += int(self.calc(num))
        return res

    # 计算长度为n的等差数列，一共有多少个子数列
    def calc(self, n):
        if n == 1:
            return 0
        n += 1
        return (n - 2) * (n - 1) / 2


print(Solution().numberOfArithmeticSlices(nums))
