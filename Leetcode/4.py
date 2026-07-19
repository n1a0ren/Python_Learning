# Q4 寻找两个正序数组的中位数 困难
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
nums1 = [1,2,3]
nums2 = [2,3,4,5]
"""
已通关
要求时间复杂度为O(log(m+n))
使用Python自带的sort()方法进行排序
最后再用简单的公式找出中位数

***时间复杂度并未达到要求，仅为O((m+n)log(m+n))
"""

if (len(nums1)+len(nums2))%2 == 0:
    even = True
else:
    even = False
combined = nums1 + nums2
combined.sort()

mid = len(combined)//2
if even:
    median = (combined[mid]+combined[mid-1])/2
else:
    median = combined[mid]