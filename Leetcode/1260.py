# Q1260 二维网格迁移 简单
# https://leetcode.cn/problems/shift-2d-grid/description/
"""
已通关
一个简单的二维数组算法，时间复杂度虽不完美，空间复杂度已达上限
本题时间与空间复杂度二者只能选其一
时间复杂度优化方案为：
展开为1维数组后一次遍历，迁移完成后打包回二维数组
"""

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

n = len(grid[0])
m = len(grid)
for time in range(k):
    top = grid[m - 1][n - 1]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if j == n-1 and i == m-1:
                continue
            elif j == n-1:
                grid[i+1][0] = grid[i][n-1]
                continue
            grid[i][j+1] = grid[i][j]
    grid[0][0] = top





"""for time in range(k):
    for i in range(n):
        for j in range(m-1):
            temp = grid[i][j]
            grid[i][j] = grid[i][j+1]
            grid[i][j+1] = temp
    for i in range(n-1):
        temp = grid[i][n-1]
        grid[i][n-1] = grid[i+1][0]
        grid[i+1][0] = temp
    temp = grid[0][0]
    grid[0][0] = grid[m-1][n-1]
    grid[m-1][n-1] = temp"""



print(grid)