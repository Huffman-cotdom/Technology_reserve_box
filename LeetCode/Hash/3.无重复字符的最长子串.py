class Solution:
    def lengthOfLongestSubstring(self, s):
        temp = {}
        left, ret = 0, 0
        for i, j in enumerate(s):
            if j in temp:
                left = max(left, temp[j] + 1)
            temp[j] = i
            ret = max(ret, i - left + 1)
        return ret


s = 'helloworld'
print(Solution().lengthOfLongestSubstring(s))
