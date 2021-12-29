# class Solution:
# 	def romanToInt(self, s):
# 		d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
# 		return sum(d.get(s[max(i - 1, 0): i + 1], d[n]) for i, n in enumerate(s))


class Solution:
    def romanToInt(self, s: str) -> int:
        # 使用字典存储所有映射可能
        d = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        # 遍历的所有结果列表, eg: "XIV" = "X" + "IV" = 10 + 4，即su = [10, 4]，最后求和
        su = []
        # s遍历开始的指针
        i = 0
        while i < len(s):
            # 优先考虑间隔两位的字符
            v = s[i:i+2]
            # 判断字符是否在d中
            if v in d:
                # 如果在，取出对应的数字
                su.append(d[v])
                # 指针跳跃一个
                i += 2                
            else:
                # 否则说明只有一个字符映射，并且一定在d中
                # 直接取出即可
                su.append(d[s[i]])
                i += 1
        # 最后对结果求和
        return sum(su)


string = 'LVIII'
print(Solution().romanToInt(string))
