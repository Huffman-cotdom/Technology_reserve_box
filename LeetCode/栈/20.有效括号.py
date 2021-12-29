class Solution:
    def isValid(self, s):
        # while '{}' in s or '()' in s or '[]' in s:
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('()', '')
        # return s == ''

        dic = {'{': '}', '(': ')', '[': ']'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)

            elif dic[stack.pop()] != c:
                return False

        return len(stack) == 1


string = "([]{})"
print(Solution().isValid(string))
