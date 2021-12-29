def maxDistance(array):
	# 记录j之前最小的a[i]
	min_ai = array[0]
	# 记录最差的差值
	max_dis = 0
	# a, b记录最大差值的下标i，j
	a, b = 0, 0
	# 暂存最大差值的i下标
	temp = 0

	for j in range(len(array)):
		# 如果小于当前的最大差值时
		if array[j] - min_ai > max_dis:
			# 更新最大差值
			max_dis = array[j] - min_ai
			a = temp
			b = j
		# 当当前位置的值小于当前最小的a[i]时
		elif array[j] - min_ai < 0:
			min_ai = array[j]
			temp = j

	return max_dis


# 函数调用格式如下
def main():
    array = [5, 3, 4, 0 ,1, 4, 1]
    dis = maxDistance(array)
    print("dis=%d," % dis)


if __name__ == '__main__':
    main()
