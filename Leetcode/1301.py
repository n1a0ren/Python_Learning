# Q1301 最大得分的路径数目 困难
# https://leetcode.cn/problems/number-of-paths-with-max-score/description/
board = ["E23","2X2","12S"]
ans = [0,0]

Max_score = 0
Max_road = 0

"""
先找临近三条的公式
再找出所有能到终点的路径
再每一条每一条路径走一遍试试
如果临近三条都是X
"""