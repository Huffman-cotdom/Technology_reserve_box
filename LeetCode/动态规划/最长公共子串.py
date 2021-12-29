class Solution:
	def longestCommonString(self, str1, str2):
		m, n = len(str1), len(str2)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		ans = 0

		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if str1[i - 1] == str2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
					ans = max(ans, dp[i][j])

		return ans


str1 = 'abcde'
str2 = 'cd'
print(Solution().longestCommonString(str1, str2))
