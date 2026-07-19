#Q3 无重复字符的最长字串 中等
#https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
s = "abcabcbcdd"

"""
已通关
模拟滑动窗口，用temp储存无重复字串后不断进行遍历，在出现重复时使用temp1记录最新无重复字串

***时间复杂度为O(n^2)，有许多优化空间
"""
Lmax = 0
temp = ""
for i in range(0,len(s)):
    temp+=(s[i])
    Tmax = 1
    if len(temp)>1:
        for j in range(0,len(temp)-1):
            if temp[-1]==temp[j]:
                temp1=""
                for k in range(j+1,len(temp)):
                    temp1+=temp[k]
                temp = temp1
                break
    Tmax = len(temp)
    if Tmax > Lmax:
        Lmax = Tmax
print(Lmax)