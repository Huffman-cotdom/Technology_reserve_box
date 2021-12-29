class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        next = self.get_next(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        return i - j if j == len(needle) else -1

    def get_next(self, t):
        n = len(t)
        nxt = [0] * (n + 1)
        nxt[0] = -1
        L, R = -1, 0
        while R < n:
            if L == -1 or t[L] == t[R]:
                L += 1
                R += 1
                nxt[R] = L
            else:
                L = nxt[L]
        return nxt


str1 = 'helloworld'
str2 = 'llo'
print(Solution().strStr(str1, str2))
