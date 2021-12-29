class Solution:
    def reverseWords(self, s):
        return ' '.join([i for i in s.split(' ') if i][::-1])


s = "the sky is blue"
print(Solution().reverseWords(s))
