class Solution:
    def longestCommonPrefix(self, strs):
        def isCommonProfix(length):
            str0 = strs[0]
            return all(str0[:length] == strs[i][:length] for i in range(1, len(strs)))

        if not strs:
            return ''

        minlen = min(len(s) for s in strs)
        low, high = 0, minlen
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonProfix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


strings = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strings))
