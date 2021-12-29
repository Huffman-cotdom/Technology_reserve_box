"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:
    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""

intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]


class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        count = 0
        intervals.sort(key=(lambda x: x[1]))
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                count += 1
            else:
                prev = intervals[i][1]
        return count


print(Solution().eraseOverlapIntervals(intervals))
