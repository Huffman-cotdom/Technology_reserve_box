class Solution:
    # 方法1：将数字转换为字符串
    # def isPalindrome(self, x):

    #     str_x = str(x)
    #     reverse_x = str_x[::-1]
    #     if reverse_x == str_x:
    #         return True
    #     else:
    #         return False

    # 方法2：将数字逆序
    def isPalindrome(self, x):
        if x < 0:
            return False

        temp, y = 0, x
        while y != 0:
            temp = temp * 10 + y % 10
            y //= 10
        return True if temp == x else False


x = 121
print(Solution().isPalindrome(x))
