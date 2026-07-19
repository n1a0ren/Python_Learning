#Homework 1
"""string = input("请输入文本：")
HUI_WEN = True
for i in range(0,len(string)//2):
        if string[i] != string[(i*-1)-1]:
            HUI_WEN = False
            break
print(HUI_WEN)"""

#Homework 2
list = []
for i in range(0,10):
    list.append(input("请输入文本："))
list.reverse()
for i in range(0,len(list)):
    list[i] = chr(ord(list[i])-32)
for i in range(0,len(list)):
    print(list[i])
