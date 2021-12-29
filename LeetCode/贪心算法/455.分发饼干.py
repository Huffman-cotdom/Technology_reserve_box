g = [2, 1, 3]
s = [1, 1]


class Solution:
    def findContentChildren(self, g, s) -> int:

        g.sort()
        s.sort()
        child = bingan = count = 0

        if (len(s) == 0) or (min(g) > max(s)):
            return 0

        while child < len(g) and bingan < len(s):
            if g[child] <= s[bingan]:
                count += 1
                child += 1
            bingan += 1

        return count


print(Solution().findContentChildren(g, s))








