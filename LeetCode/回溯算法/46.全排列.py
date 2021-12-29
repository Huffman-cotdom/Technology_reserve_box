# class Solution:
# 	def permute(self, nums):
# 		def backtrack(first = 0):
# 			# 如果所有的数都填完了
# 			if first == n:
# 				res.append(nums[:])
# 			for i in range(first, n):
# 				# 动态维护数组
# 				nums[first], nums[i] = nums[i], nums[first]
# 				# 继续递归填下一个数
# 				backtrack(first + 1)
# 				# 撤销操作
# 				nums[first], nums[i] = nums[i], nums[first]

# 		n = len(nums)
# 		res = []
# 		backtrack()
# 		return res

class Solution:
    def permute(self, nums):
        # 因为最终目的是获得一个装有列表的列表
        # 因此我们初始化一个空列表
        res = []
        # 接着我们需要编写一个内置函数，这个函数接下来会被调用
        # 回溯法的递归方式是在内置函数的外部和内部分别调用它，来保证回溯
        # 你需要把它想象成二叉树的深度优先遍历，外部的调用类似每个"深度"的遍历
        # 而内部调用就是真正深度的遍历，当然深度的遍历是必须带有结束条件的
        def backtrack(nums, tmp):
            """这个内置函数以输入的待排列list为第一个参数
               第二个参数则是在搜索过程中不断累加的可能结果
               它的初始化是一个空列表
            """
            # 首先需要明确深度遍历的结束条件
            # 就是nums已经为空
            if not nums:
                # 这时说明已经到了足够的深度，tmp已经完成这条路径的采集
                res.append(tmp)
                return 
            # 如果nums还不是空的，我们会遍历nums
            # 第一次的nums遍历就是被外部调用，类似每个"深度"的遍历
            # 这并不会是nums的数量减小，而是逐个的遍历而已
            for i in range(len(nums)):
                # 接下来，我们在逐个遍历时，又一次调用这个函数
                # 只不过这一次该函数的输入变成了除去"i"位置的其他数值
                # 因此我们发现，内置的调用会让nums的元素越来越少，直到满足终止条件
                # 并且，原来的tmp开始使用正在遍历的元素进行累加（列表的合并）
                # 也就是说，直到"深度"遍历完，tmp会收集到所有的nums中的数值
                # 因此，tmp成为nums中的一种排列的可能被存到res结果列表中
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        # 外部调用
        backtrack(nums, [])
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
