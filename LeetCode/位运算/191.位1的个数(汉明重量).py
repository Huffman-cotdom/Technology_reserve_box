"""
    n & (n−1)，其预算结果恰为把 nn 的二进制位中的最低位的 11 变为 00 之后的结果
    如：6 & (6 - 1) = 4, 6 = (110), 4 = (100), 运算结果4即把6的二进制位中的最低位1变为0之后的结果
"""
num = 30


class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret


print(Solution().hammingWeight(num))
