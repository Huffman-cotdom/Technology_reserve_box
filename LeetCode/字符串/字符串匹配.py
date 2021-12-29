# 给定一个 haystack 字符串和一个 needle 字符串，
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。

class Solution:
    def pattern(self, str1, str2):
        return str1.index(str2) if str2 in str1 else -1


str1 = 'hello'
str2 = 'll'
print(Solution().pattern(str1, str2))
