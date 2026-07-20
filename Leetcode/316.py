# Q316 去除重复字母
# https://leetcode.cn/problems/remove-duplicate-letters/description/
s = "acbac"

string = list(s)
ans = list()
for i in range(len(s)):
    if not ans:
        ans.append(string[i])
        string[i] = ""
        continue
    elif string[i] == ans[-1]:
        string[i] = ""
        continue
    elif string[i] in ans:
        string[i] = ""
        continue
    elif string[i] > ans[-1]:
        ans.append(string[i])
        string[i] = ""
        continue
    else:
        while True:
            if not ans:
                ans.append(string[i])
                string[i] = ""
                break
            if ans[-1] in string and string[i] < ans[-1]:
                ans.pop()
            else:
                ans.append(string[i])
                string[i] = ""
                break
Sans = ''
for char in ans:
    Sans+=char
print(Sans)