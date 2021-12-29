class Solution:
    def lengthOfLastWord(self, s):
        x = s.split()
        if s:
            return len(x[-1])
        else:
            return 0


s = "Hello World"
print(Solution().lengthOfLastWord(s))
