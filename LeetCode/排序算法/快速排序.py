# def Partition(arr, low, high):
#     temp = arr[high]
#     i = low - 1     # 最小元素索引

#     for j in range(low, high):
#         if arr[j] <= temp:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def QuickSort(arr, low, high):
#     if low < high:
#         p = Partition(arr, low, high)

#         QuickSort(arr, low, p - 1)
#         QuickSort(arr, p + 1, high)

class Solution:
    def Partition(self, arr, low, high):
        temp = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= temp:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def QuickSort(self, arr, low, high):
        if low < high:
            p = self.Partition(arr, low, high)

            self.QuickSort(arr, low, p - 1)
            self.QuickSort(arr, p + 1, high)


arr = [6, 8, 7, 9, 0, 1, 3, 2, 4, 5]
Solution().QuickSort(arr, 0, len(arr) - 1)
print("排序之后的数组为：", arr)
