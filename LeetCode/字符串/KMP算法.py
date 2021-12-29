class Solution:
	def strStr(self, haystack, needle):
		h_len, n_len = len(haystack), len(needle)
		if n_len == 0:
			return 0
		next = self.get_next(needle)
		i, j = 0, 0
		while i < h_len and j < n_len:
			if j == -1 or haystack[i] == needle[j]:
				i += 1
				j += 1
			else:
				j = next[j]
		# j指针遍历了t
		if j == n_len:
			return i - j
		return -1


	def get_next(self, needle):
		n = len(needle)
		next = [0 for _ in range(n + 1)]
		next[0] = -1
		l = -1
		r = 0
		while r < n:
			if l == -1 or needle[l] == needle[r]:
				l += 1
				r += 1
				next[r] = l
			else:
				l = next[l]
		return next


str1, str2 = 'helloworld', 'llowo'
print(Solution().strStr(str1, str2))
