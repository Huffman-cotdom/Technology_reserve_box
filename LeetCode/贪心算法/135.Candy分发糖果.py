"""
老师想给孩子们分发糖果，有N个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
    每个孩子至少分配到 1 个糖果。
    评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果
"""
ratings = [1, 0, 2]


class Solution:
    def candy(self, ratings):
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                right[i] = right[i + 1] + 1
        return sum(max(left[i], right[i]) for i in range(len(ratings)))


print(Solution().candy(ratings))
