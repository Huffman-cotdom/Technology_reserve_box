# 异或运算的特点：
# a ^ 0 = a
# a ^ a = 0
# a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b
import functools


def onlyOneTimeNumber(array):
	# ans = 0
	# for i in array:
	# 	ans ^= i

	# return ans

	# ret = 2 & 10 = 8
	ret = functools.reduce(lambda x, y: x ^ y, array)

	div = 1
	while div & ret == 0:
	    div <<= 1
	a, b = 0, 0
	for arr in array:
	    if arr & div:
	        a ^= arr
	    else:
	        b ^= arr
	return [a, b]


# 函数调用格式如下
def main():
    array = [1, 2, 10, 4, 1, 4, 3, 3]
    num = onlyOneTimeNumber(array)
    print(num)


if __name__ == '__main__':
    main()
