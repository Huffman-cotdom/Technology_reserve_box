class Solution:
    def get_num(self, string, s):

        return len(string.lower().split(s.lower())) - 1


string = 'AA12vs'
s = 'a'
print(Solution().get_num(string, s))
