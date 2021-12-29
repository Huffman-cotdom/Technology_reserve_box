class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix:
            return 0

        h, w = len(matrix), len(matrix[0])

        store = [[None]*(w) for _ in range(h)]

        m = 0  # 储存max路径值

        def search_nearby(i, j):
            nonlocal m

            compare = []  # 储存可以比较的候选人

            # 上
            if i != 0 and matrix[i-1][j] < matrix[i][j]:  # 有上边且上边小于当前数的话
                compare.append(
                    store[i-1][j]) if store[i-1][j] else compare.append(search_nearby(i-1, j))

            # 左
            if j != 0 and matrix[i][j-1] < matrix[i][j]:  # 有左边且左边小于当前数的话
                compare.append(store[i][j-1]) if store[i][j -
                                                          1] else compare.append(search_nearby(i, j-1))

            # 下
            if i != h-1 and matrix[i+1][j] < matrix[i][j]:  # 有下边且下边小于当前数的话
                compare.append(
                    store[i+1][j]) if store[i+1][j] else compare.append(search_nearby(i+1, j))

            # 右
            if j != w-1 and matrix[i][j+1] < matrix[i][j]:  # 有右边且右边小于当前数的话
                compare.append(store[i][j+1]) if store[i][j +
                                                          1] else compare.append(search_nearby(i, j+1))

            store[i][j] = max(compare)+1 if compare else 1
            # 如果没有compare说明这是一个很小的数，是一个起始点，能组成的长度只有1
            # 有的话就原来最长路径+1

            m = max(m, store[i][j])
            return (store[i][j])

        for i in range(h):
            for j in range(w):
                if not store[i][j]:
                    search_nearby(i, j)

        return m


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(Solution().longestIncreasingPath(matrix))
