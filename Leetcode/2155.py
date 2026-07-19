#Q2155 分组得分最高的所有下标 中等
#https://leetcode.cn/problems/all-divisions-with-the-highest-score-of-a-binary-array/description/
nums = [0]
"""
已通关
这次使用了滑动窗口，先给予一个初始值，然后每滑动一次便更新一次状态，避免了内部的循环嵌套和计算冗余
"""
left = 0
right = MaxScore = nums.count(1)
iList = [0]
for i in range(1,len(nums)+1):
    if nums[i-1]==1:
        right -= 1
    else:
        left +=1
    if right+left>MaxScore:
        MaxScore = right+left
        iList.clear()
        iList.append(i)
    elif right+left==MaxScore:
        iList.append(i)
print(iList,MaxScore)

#逻辑有误再次失败放弃
"""iList = []
Max_score = 0
i = len(nums)//2

while 0 < i <= len(nums):
    right = left = Tleft = Tright = 0
    #查询numleft和numright的分数
    for j in range(0,i):
        if nums[j]==0:
            left+=1
        else: Tleft+=1
    for j in range(i,len(nums)):
        if nums[j]==1:
            right += 1
        else: Tright+=1
    #如果numleft和numright的分数大于Max_score就执行操作
    if left+right==Max_score:
        iList.append(i)
    elif left+right>Max_score:
        Max_score = left + right
        iList.clear()
        iList.append(i)
    #在假设left和right仍有优化空间的情况下继续遍历
    if (left-Tleft)-(right-Tright) == 0:
        iList.append(i)
    elif (left-Tleft)-(right-Tright) > (right-Tright)-(left-Tleft):
        i = i + ((len(nums) - i) // 2 + 1)
    else: i = i//2
score=0
if i == 0:
    for j in range(0,len(nums)):
        if nums[j]==1:
            score+=1
if score==Max_score:
    iList.append(i)
elif score>Max_score:
    iList.clear()
    iList.append(i)
if not iList:
    iList.append(i)"""


#时间复杂度On^2，时间测试未通关
"""iList = []
Max_score = 0
for i in range(0,len(nums)+1):
    score = 0
    for j in range(i-1,-1,-1):
        if nums[j] == 0:
            score+=1
    for j in range(i,len(nums)):
        if nums[j] == 1:
            score+=1
    if score>Max_score:
        Max_score = score
        iList.clear()
        iList.append(i)
    elif score == Max_score:
        iList.append(i)
print(Max_score, iList)"""