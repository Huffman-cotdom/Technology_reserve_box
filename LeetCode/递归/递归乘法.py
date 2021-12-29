# 递归乘法。 写一个递归函数，不使用 * 运算符，
# 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

class Solution:
    def multiply(self, A, B):
        if A == 0 or B == 0:
            return 0

        if A < B:
            return B + self.multiply(A - 1, B)

        return A + self.multiply(A, B - 1)


A, B = 2, 5
print(Solution().multiply(A, B))
