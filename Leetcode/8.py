# Q8 字符串转换整数 中等
# https://leetcode.cn/problems/string-to-integer-atoi/description/
import math
s = "   +0 123"
read = ""
for char in s:
    if not read and char == " ":
        continue
    if not read and (char == "-" or char == "+") :
        read += char
        continue
    if 48<=ord(char)<=57:
        read += char
    else:
        break
if read and (len(read)>=2 or (read[0]!="+" and read[0]!="-")):
    read = int(read)
    if read<math.pow(2,31)*-1:
        read = int(math.pow(2,31)*-1)
    elif read>math.pow(2,31)-1:
        read = int(math.pow(2,31)-1)
else:
    read = 0
print(read)