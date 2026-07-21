# Q509 斐波那契数
# https://leetcode.cn/problems/fibonacci-number/
n=10

#用数据容器做记忆体（熟悉的方法）
numDict = {}
def f(n):
    if n<=1:
        return n
    elif n in numDict:
        return numDict[n]
    else:
        numDict[n]=f(n-1)+f(n-2)
        return numDict[n]
print(f(100))

#用变量存储动态结构（不熟悉的方法）
"""def f(n):
    if n<=1:
        return n
    else:
        a,b = 0,1
        # a和b依旧分别代表f(n-1)和f(n)
        for i in range(n-1):
            a,b = b,a+b
        return b"""

"""
其实和爬楼梯的题目内容特别相近，只不过边界数值改了一改
斐波那契数的边界数值是f(0)=0,f(1)=1
而最关键的状态转移公式依旧是f(n)=f(n-1)+f(n-2)
"""