# Q32 最长有效括号 困难
# https://leetcode.cn/problems/longest-valid-parentheses/
s = "((())))((()()"

"""
已通关
使用了双向遍历（双指针），由左至右遍历一次，再由右至左遍历一次
假设左括号多过右括号，必定有左括号不在有效括号组内，右至左的遍历即可处理这一情况，反之亦然
最后用Lmax储存最大括号长度
"""
Lmax = 0
left = 0
right = 0
for char in s:
    if char == "(":
        left += 1
    else:
        right += 1
    if right > left:
        left = 0
        right = 0
    elif left == right:
        Lmax = max(Lmax, right * 2)

left = 0
right = 0

for char in reversed(s):
    if char == "(":
        left += 1
    else:
        right += 1
    if left > right:
        left = 0
        right = 0
    elif left == right:
        Lmax = max(Lmax, left * 2)

print(Lmax)