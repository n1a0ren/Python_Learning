# Q5 最长回文（对称）字串 中等
# https://leetcode.cn/problems/longest-palindromic-substring/description/
s = "babad"

"""
已通关
使用了中心扩展法，先找到一个对称字串，然后向外扩展，每扩展一步进行一次更新，最后记录最长的字串

***仍有优化时间复杂度的空间，使用动态规划，或马拉车算法
"""
def expand(s, start, end):
    times = 0
    while True:
        if not (start - 1 < 0 or end + 1 >= len(s)):
            if s[start - 1] == s[end + 1]:
                times += 1
                start -= 1
                end += 1
            else:
                break
        else:
            break
    print(times)
Lmax = 0
start = 0
end = 0

# 寻找长度为2的回文字串
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        temp = 2
        # 当前二个或后二个字符为回文字串时
        if i == 0:
            if temp >= Lmax:
                Lmax = temp
                start = i
                end = i + 1
        elif i + 1 == len(s) - 1:
            if temp >= Lmax:
                Lmax = temp
                start = i
                end = i + 1
        # 开始扩圈
        else:
            times = expand(s, i, i + 1)
            temp += (times * 2)
            if temp >= Lmax:
                Lmax = temp
                start = i - times
                end = i + 1 + times

# 寻找长度为3的回文字串
for i in range(0, len(s) - 2):
    if s[i] == s[i + 2]:
        temp = 3
        # 当前二个或后二个字符为回文字串时
        if i == 0:
            if temp >= Lmax:
                Lmax = temp
                start = i
                end = i + 2
        elif i + 2 == len(s) - 1:
            if temp >= Lmax:
                Lmax = temp
                start = i
                end = i + 2
        # 开始扩圈
        else:
            times = expand(s, i, i + 2)
            temp += (times * 2)
            if temp >= Lmax:
                Lmax = temp
                start = i - times
                end = i + 2 + times

print(Lmax)
ans = ""
for i in range(start, end + 1):
    ans += s[i]
print(ans)

