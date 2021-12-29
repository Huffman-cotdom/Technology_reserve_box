M = int(input())
nums = []
for i in range(M):
	nums.append(int(input()))
N = int(input())


def N_nums(nums, N):
	length = len(nums)
	if len(set(nums)) < length:
		return -1
	res = 0
	nums.sort()
	for i in range(N):
		res += nums[i]
	nums.sort(reverse=True)
	for i in range(N):
		res += nums[i]
	return res


print(N_nums(nums, N))
