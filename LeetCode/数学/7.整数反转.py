# class Solution():
#     def reverse(self, x):
#         if -10 < x < 10:
#             return x
#         x_str = str(x)
#         if x_str[0] == '-':
#             x_str = x_str[:0:-1]
#             x = int(x_str)
#             x = -x
#         else:
#             x_str = x_str[::-1]
#             x = int(x_str)
#         return x if -2147483648 <= x <= 2147483648 else 0


class Solution():
    def reverse(self, x):
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        abs_x, temp = abs(x), 0
        while abs_x != 0:
            temp = temp * 10 + abs_x % 10
            if temp > boundry:
                return 0
            abs_x //= 10
        return temp if x > 0 else -temp


x = -9
print(Solution().reverse(x))
