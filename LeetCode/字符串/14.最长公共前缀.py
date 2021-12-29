class Solution:
    # 方法1：横向遍历
    # def longestCommonPrefix(self, strs):
    #     if not strs:
    #         return ''

    #     profix = strs[0]
    #     for i in range(1, len(strs)):
    #         profix = self.lcp(profix, strs[i])
    #         if not profix:
    #             break

    #     return profix

    # def lcp(self, str1, str2):
    #     minlen = min(len(str1), len(str2))
    #     index = 0
    #     while index < minlen and str1[index] == str2[index]:
    #         index += 1

    #     return str1[:index]

    # 方法2：纵向遍历
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        for i in range(len(strs[0])):
            char = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != char for j in range(1, len(strs))):
                return strs[0][:i]

        return strs[0]


strings = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strings))
