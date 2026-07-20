# Q1301 最大得分的路径数目 困难
# https://leetcode.cn/problems/number-of-paths-with-max-score/description/

"""
已通关
用时3小时，时间复杂度和空间复杂度都有大问题
对动态规划的大考验，我的方法是开一个dict去当做缓存，直接提取计算过的所需数据
卡关位置有三，
第一：动态规划的状态转移公式，
第二：代码实现动态规划的能力太差，代码搓的太慢
第三：将两种元素同时在动态规划中保持更新，这是以前从未做过的题型（最高分数和路径总数）
"""

board = ["E5973","52912","38217","61335","5595S"]
n = len(board)-1

#scoreDict, key = 格子坐标，value = (到达该格子的最大得分数, 得到最大得分数的路径数目)
scoreDict = {(n,n):[0,1]}
def getScore(board, x, y):
    if x>n or y>n:
        return [-1,0]
    if board[x][y] == "X":
        return [-1,0]
    if (x,y) in scoreDict:
        return scoreDict[(x,y)]
    else:
        scoreDict[(x,y)] = getMaxScore(board,x,y)
        return scoreDict[(x,y)]

def getMaxScore(board,x,y):

    if board[x][y] == "X":
        return [-1,0]

    left = getScore(board,x,y+1)
    up = getScore(board,x+1,y)
    diagonal = getScore(board,x+1,y+1)
    best = max(left[0], up[0], diagonal[0])
    if best == -1:
        return [-1,0]

    path = 0
    if left[0] == best:
        path+=left[1]
    if up[0] == best:
        path+=up[1]
    if diagonal[0] == best:
        path += diagonal[1]

    if board[x][y] == "E" or board[x][y] == "S":
        return [best% (10**9+7),path% (10**9+7)]
    else:
        return [best+int(board[x][y]),path]

print(getScore(board,0,0))
print(scoreDict)



"""def getMaxWay(board,x,y):
    if board[x][y] == "X":
        return 0
    if x>=n or y>=n:
        return 0
    way = 0
    left = getMaxScore(board,x,y+1)
    up = getMaxScore(board,x+1,y)
    diagonal = getMaxScore(board,x+1,y+1)
    Max_Score = max(left,up,diagonal)
    if left == Max_Score:
        way += 1
    if up == Max_Score:
        way += 1
    if diagonal == Max_Score:
        way += 1
    return way"""

#可惜，分数找对了，但是路径数没有跟着同步，并且对障碍的逻辑仍有谬误
"""def getMaxScore(board,x,y):
    if board[x][y] == "X":
        return 0
    elif board[x][y] == "E" or board[x][y] == "S":
        return max(getScore(board, x + 1, y), getScore(board, x, y + 1), getScore(board, x + 1, y + 1))
    else:
        return max(getScore(board,x+1,y),getScore(board,x,y+1),getScore(board,x+1,y+1))+int(board[x][y])

def getScore(board, x, y):
    if x>n or y>n:
        return 0
    if board[x][y] == "X":
        return 0
    if (x,y) in scoreDict:
        return scoreDict[(x,y)][0]
    else:
        scoreDict[(x,y)] = [getMaxScore(board,x,y),1]
        return scoreDict[(x,y)][0]

def getMaxWay(board,x,y):
    if board[x][y] == "X":
        return 0
    if x>n or y>n:
        return 0
    way = 0
    left = getMaxScore(board,x,y+1)
    up = getMaxScore(board,x+1,y)
    diagonal = getMaxScore(board,x+1,y+1)
    Max_Score = max(left,up,diagonal)
    if left == Max_Score:
        way += 1
    if up == Max_Score:
        way += 1
    if diagonal == Max_Score:
        way += 1
    return way

for i in range(0,n+1):
    for j in range(0,n+1):
        if (i,j) not in scoreDict or scoreDict[(i,j)][0] < getMaxScore(board, i,j):
            scoreDict[(i,j)] = [getMaxScore(board, i,j),1]
        elif scoreDict[(i,j)][0] == getMaxScore(board, i,j):
            scoreDict[(i,j)][1] += 1

scoreDict[(0,0)][1] = getMaxWay(board,0,0)
print(getScore(board,0,0))
print(scoreDict)"""




"""def getScore(board,m,n):
    #当到达终点时，直接返回
    if m == 0 or n == 0:
        return scoreDict[(m,n)]
    #当到达障碍时，返回0
    if board[m][n] == "X":
        return (0,0)
    #如果字典能找到，直接返回字典
    if (m,n) in scoreDict:
        return scoreDict[(m,n)]

    else:
        scoreDict[(m,n)] = getScore(board,m,n)
        return scoreDict[(m,n)]"""

"""def findTotalWay(board, m, n):
    # 处理边界数据
    if m < 0 or n < 0:
        return -1

    # 到终点
    if m == 0 or n == 0:
        return 1

    # 如果参数的位置在字典里，直接调用
    if (m,n) in wayDict:
        return wayDict[(m,n)]

    # 如果参数的位置不在字典里，往下切割小问题后找到参数数值，塞进字典后return
    else:
        wayDict[(m,n)] = (findTotalWay(board, m, n-1)+
                          findTotalWay(board, m-1, n-1)+
                          findTotalWay(board, m-1, n))
        return wayDict[(m,n)]
        
print(findTotalWay(board,99,99))"""

"""
先找临近三条的公式
再找出所有能到终点的路径

假设所处位置是board[m][n]
向上走一格就是m-1
向左走一格就是n-1
向斜走一个就是m-1,n-1
Start是board[2][2]
最终要做到board[0][0]
也就是找m,n有多少种方法可以减成0

子结构board[m-1][n-1]
状态转换公式 board[x][y] = board[x+1][y+1] + board[x+1][y] + board[x][y+1]

根据Leet的提示，在动态规划中可以为每一个格子维护2个信息：到达该格子的最大得分，到达该最大得分的路径数目
"""