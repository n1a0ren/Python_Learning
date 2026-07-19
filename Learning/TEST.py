s = ")(())))(())())"

max_len = 0
left = 0
right = 0

# 1. 从左到右遍历
for char in s:
    if char == '(':
        left += 1
    else:
        right += 1

    if left == right:
        max_len = max(max_len, 2 * right)
    elif right > left:
        # 右括号多于左括号，说明当前子串无效，重置
        left = right = 0

left = right = 0

# 2. 从右到左遍历
for char in reversed(s):
    if char == '(':
        left += 1
    else:
        right += 1

    if left == right:
        max_len = max(max_len, 2 * left)
    elif left > right:
        # 左括号多于右括号，说明当前子串无效，重置
        left = right = 0

print(max_len)