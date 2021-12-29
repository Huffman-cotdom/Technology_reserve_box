def ballSort(nums):
    begin, curr, end = 0, 0, len(nums) - 1
    while curr <= end:
        if nums[curr] == 0:
            nums[begin], nums[curr] = nums[curr], nums[begin]
            begin += 1
            curr += 1

        elif nums[curr] == 1:
            curr += 1

        else:
            nums[curr], nums[end] = nums[end], nums[curr]
            end -= 1


nums = [1, 2, 1, 0, 1, 2, 0, 0, 1, 2]
ballSort(nums)
print(nums)
