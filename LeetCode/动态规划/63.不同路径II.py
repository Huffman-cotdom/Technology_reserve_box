class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 新建矩阵版
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        store = [[0] * width for _ in range(height)]

        # 从上到下，从左到右
        for m in range(height):
            for n in range(width):
                # 如果这一格没有障碍物
                if not obstacleGrid[m][n]:
                    if m == n == 0:
                        store[m][n] = 1
                    else:
                        a = store[m - 1][n] if m != 0 else 0
                        b = store[m][n - 1] if n != 0 else 0
                        store[m][n] = a + b
        return store[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))
