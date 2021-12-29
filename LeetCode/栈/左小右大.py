def get_point_number(arr):
    # 定义一个栈存储index
    stack = list()
    # 记录栈中的最大值
    max_num = -int(1e9)
    for i in range(len(arr)):

        # 当栈不为空，并且arr中当前位置的值小于等于栈中保存的最后的位置的值时，将栈中最后一个元素pop
        while len(stack) != 0 and arr[stack[len(stack) - 1]] >= arr[i]:
            stack.pop()

        if arr[i] > max_num:
            stack.append(i)

        # 维护最大值
        max_num = max(max_num, arr[i])

    return stack


# 函数调用格式如下
def main():
    a = [2, 1, 3, 4, 5, 7, 6]
    res = get_point_number(a)
    print(res)


if __name__ == '__main__':
    main()
