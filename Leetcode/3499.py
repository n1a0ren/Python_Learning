# Q3499 操作后最大活跃区段数I
# https://leetcode.cn/problems/maximize-active-section-with-trade-i/description/
s = "1000111010"

"""
已通关
时间复杂度为O(n^2)，但可优化为O(N)
思路大致方向正确，但在代码实现上出现问题
我的思路是找到两个被1隔开且被1包围的连续0，并用了复杂的“三关”去实现
但完全可以在一次遍历中，找到每一段连续0的长度，邻邻相加，最后返回最大值

在解题思路上没有问题，但代码实现和思考的复杂度仍有待优化
"""
t=["1"]+list(s)+["1"]
start,end, Max_extra= 0,1,0

firstKey, secondKey, thirdKey = False,False,False
temp = 0
while start<len(t) and end<len(t):
    if t[start]=="1":
        if not firstKey:
            if t[end]=="0":
                firstKey = True #第一关通过
                end+=1
                continue
            else:
                start=end
                end+=1
                continue
        if not secondKey:
            if t[end]=="1":
                temp+=1
                secondKey = True #第二关通过
                end+=1
                continue
            else:
                end+=1
                continue
        if not thirdKey:
            if t[end]=="0":
                thirdKey = True
                end += 1
                continue
            else:
                temp += 1
                end += 1
                continue
        if firstKey and secondKey and thirdKey:
            if t[end]=="1":
                Max_extra = max(end-start-temp-1, Max_extra)
                firstKey, secondKey, thirdKey = False,False,False
                temp = 0
                start+=1
                end=start+1
                continue
            else:
                end+=1
                continue
    else:
        start+=1
        end+=1
print(t)
print(t.count("1")+Max_extra-2)

"""
选择一个被0包围的1区段，将里面的1全部转为0，再将一个被1包围的0区段全部转为1
找出最大活跃区段的可能性，最后返回1的总数

最大活跃区段数=原活跃区段数+0转换为1的数
原活跃区段数指字符串自带的1的数目
0转换为1的数就是在一次操作中增加了多少个1

根据题意可得：被0包围的连续“1”，可以将里面的1全部转为0，而这个包围连续“1”的0也需被“1”包围
这样才能完整进行一次操作
而最大的0转1数目，就是这个被1包围的连续0中有多少个0
这个连续0中间必须且仅能包含一次连续1

共设三个关卡
第一关：start后的数字需是0
第二关：0之后可以碰见1
第三关：0在碰见1后又撞回0
等再碰到一次1，就结束
"""
