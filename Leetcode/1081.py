# Q1081 不同字符的最小字典序子序列 中等
# https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/description/

"""
已通关
因为If...elif...else的逻辑判断前后出错，导致卡了很久
记得在If逻辑判断时注意前后顺序，否则会进入错误的入口
Continue关键字可以直接结束当前这一次循环，进行下一次循环
"""

s = "cdebacdcbc"

string = list(s)
temp = []

for i in range(len(string)):

    # 当遍历到的字符已经在temp，直接置空string
    if string[i] in temp:
        string[i] = ''
        continue

    # 当遍历到的字符大于最后一个，或者temp为空，直接进temp，并且置空string
    elif (not temp) or string[i]>temp[-1]:
        temp.append(string[i])
        string[i] = ''
        continue

    elif string[i]<temp[-1]:
        # 当遍历到的字符小于最后一个
        while temp and string[i]<temp[-1]:
            # 如果最后一个字符在string中还有剩，就pop掉
            if string.count(temp[-1])>0:
                temp.pop()
            # 如果最后一个字符在string中没有了，就直接进去
            else:
                break
        if string[i] not in temp:
            temp.append(string[i])
            string[i] = ''
        continue

print("".join(temp))








"""Tans = []
temp = []
for char in s:
    temp.append(char)

for i in range(0,len(temp)):
    print(Tans,"外")
    if not Tans:
        Tans.append(temp[i])
        temp[i]=''
    elif Tans[-1]>temp[i]:
        Tans.append(temp[i])
        temp[i] = ''
    else:
        idx=-1
        while idx>=-len(temp) and Tans[idx]<temp[i]:
            if temp.count(Tans[idx])>0:
                Tans.pop()
            idx-=1
            print(Tans, "内", temp[i])
            if temp.count(temp[i])<2 and idx==-len(temp):
                Tans.append(temp[i])
                temp[i] = ''
                break
            if not Tans:
                Tans.append(temp[i])
                temp[i] = ''
                break

print(Tans)"""


"""    elif not temp.count(temp[i])>1 and not Tans.count(temp[i]):
        Tans.append(temp[i])
        temp[i] = ''"""







"""smallest = 999
temp = []
idx = 0
for char in s:
    print(temp)
    if ord(char)<smallest:
        smallest = ord(char)
        idx = len(temp)
        temp.append(char)
    elif ord(char)==smallest:
        pass
    else:
        if char in temp:
            if ord(char)>smallest and (charIDX(temp,char)):
                print("idx-1")
                idx-=1
                temp.remove(char)
                temp.append(char)
        else: temp.append(char)
ans = ''
for char in temp:
    ans+=char

print(temp, smallest, ans, idx)
def charIDX(temp,char1):
    for i in range(0,len(temp)):
        if temp[i] == char1:
            if i+1>=len(temp) and ord(temp[i])>ord(temp[i+1]):
                return True
    return False"""


