class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        res = []
        # 顺时针方向
        around = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 四个方向的边界
        left, right, top, bottom = c0 - 1, c0 + 1, r0 - 1, r0 + 1
        # (x, y)为当前节点，num为当前查找的数字，Dir为当前的方向
        x, y, num, Dir = r0, c0, 1, 0
        while num <= R * C:
            # (x, y)在矩阵中
            if x >= 0 and x < R and y >= 0 and y < C:
                res.append([x, y])
                num += 1
            # 向右到右边界
            if Dir == 0 and y == right:
                # 调整方向向下
                Dir += 1
                # 右边界右移
                right += 1
            # 向下到底边界
            elif Dir == 1 and x == bottom:
                Dir += 1
                # 底边界下移
                bottom += 1
            # 向左到左边界
            elif Dir == 2 and y == left:
                Dir += 1
                # 左边界左移
                left -= 1
            # 向上到上边界
            elif Dir == 3 and x == top:
                Dir += 1
                # 上边界上移
                top -= 1
            x += around[Dir][0]
            y += around[Dir][1]
        return res


print(Solution().spiralMatrixIII(2, 3, 1, 1))
