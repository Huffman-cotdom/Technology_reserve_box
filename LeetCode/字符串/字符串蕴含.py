# 给定以下字符串：
# input = "helloword" target = "ell"
# 如果target在input中，则返回其在input中的首字母下标列表，否则返回空列表。

class Solution:
    def search(self, input, target):
        i = 0
        res = []
        while i < len(input) - len(target):
            j = 0
            while j < len(target):
                if input[i + j] == target[j]:
                    if j == len(target) - 1:
                        res.append(i)
                    j += 1
                else:
                    break
            i += 1
        return res


input = 'helloworld'
target = 'ell'
print(Solution().search(input, target))
