class Solution:
    def getLeastNumbers(self, arr, k):
        arr.sort()
        return arr[:k]


arr = [3, 2, 1, 4]
k = 2
print(Solution().getLeastNumbers(arr, k))
