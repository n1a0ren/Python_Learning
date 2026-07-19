# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
"""
当n=10，青蛙想跳上10级时只能从第八级或者第九级跳上去
那n=10的跳法其实就等于n=9+n=8
改善一下写法，f(10)=f(9)+f(8)
f(9)=f(7)+f(8)
f(10)=f(8)+f(8)+f(7)
f8 = f7+f6
f10 = f6*2+f7*3
...
这种算法会导致多余计算
如上可见f6计算了2遍，f7计算了3遍，下面的f1f2更是会有指数级的计算量上升

而为了减少这种多余计算，我们可以开一个新的数据容器，用于存储将来要再次使用的数据，无需再次计算
让我们开一个dictionary，在f3,f4,f5...这些第一次被计算后，便存入dictionary
而以后在计算f(n)需要调用时，直接从dictionary中提取即可

真正的难点在定义状态以及找到状态转移方程，这些就需要多加练习
"""


# 暴力递归演示
def getWaysRedundant(num):
    if num==1:
        return 1
    if num==2:
        return 2
    return(getWaysRedundant(num-2)+getWaysRedundant(num-1))
#print(getWaysRedundant(100))

# 动态规划演示
# 由顶至下开始拆解
# 时间复杂度为最优解O(n)，但空间复杂度并非最优解O(1)，而是O(n)
def getWaysDynamic(num, wayDict = {1 : 1, 2 : 2}):
    if num in wayDict:
        return wayDict[num]
    elif num<=0:
        return -1
    else :
        result = getWaysDynamic(num-1)+getWaysDynamic(num-2)
        wayDict[num] = result
        return result

"""
动态规划有4个重点：最优子结构、状态转移方程、边界、重叠子问题
本题中，f(n)的最优子结构为f(n-1)和f(n-2)
状态转移方程为f(n)=f(n-1)+f(n-2)
边界为f(1)和f(2)
重叠子问题 例如f(10)=f(9)+f(8)=f(8)+f(8)+f(7)，这里f(8)就是重叠子问题
"""

#自底向上
#时间复杂度O(n)和空间复杂度O(1)都是最优解版本
#仅用两个变量解决不断重叠的子问题，因为重叠子问题最多只能同时出现两个
def getWaysBest(num):
    if num < 1:
        return -1
    if num == 1:
        return 1
    if num == 2:
        return 2
    a = 1 #此为单数格的缓存 3
    b = 2 #此为双数格的缓存
    for i in range(2,num):
        if i%2>0:
            b = b+a
        else:
            a = a+b
    return max(a,b)

num = 8
print(getWaysRedundant(num))
print(getWaysDynamic(num))
print(getWaysBest(num))

"""
动态规划的解题思路就是：复杂问题拆分子问题，记住过往的计算，减少重复计算

动态规划解题思路的顺序：
1. 穷举分析
当台阶是1级，只有一种跳法；当台阶是2级，只有2种跳法
而台阶是3级时，便能由第一级跳上去，或由第二级跳上去
4级时同样如此，这样便是穷举分析，穷举出一切的可能性

2. 确定边界
边界即是不会变动的常数
例如本题，通过穷举分析，边界确定为f(1)和f(2)

3. 找规律（找出子结构）
n>=3时，从穷举分析中已经可以看出，f(n)的子结构为f(n-1)和f(n-2)

4. 写出状态转移的方程
状态转移即是将子结构转换为目标结构
f(n)（目标）= f(n-1)（子结构）+f(n-2)（子结构）

5. 代码实现
"""
