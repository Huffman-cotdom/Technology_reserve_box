# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。

class Solution:
    def addBinary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        return bin(x + y)[2:]


a, b = 11, 1
a, b = bin(a), bin(b)
print(Solution().addBinary(a, b))
