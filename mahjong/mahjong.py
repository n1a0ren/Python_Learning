import random

PAI_SHAN = []
HU = False

#字牌
for i in range(0,4):
    PAI_SHAN.append("Df")
    PAI_SHAN.append("Nf")
    PAI_SHAN.append("Xf")
    PAI_SHAN.append("Bf")
    PAI_SHAN.append("BB")
    PAI_SHAN.append("HZ")
    PAI_SHAN.append("FC")

#万索饼
for j in range(1,10):
    for i in range(0,4):
        PAI_SHAN.append(str(j)+"p")
        PAI_SHAN.append(str(j)+"s")
        PAI_SHAN.append(str(j)+"m")

#红宝牌
PAI_SHAN.remove("5p")
PAI_SHAN.remove("5s")
PAI_SHAN.remove("5m")
PAI_SHAN.append("0p")
PAI_SHAN.append("0s")
PAI_SHAN.append("0m")

#打乱
inGame_PAISHAN = []
while PAI_SHAN:
    tmp = random.choice(PAI_SHAN)
    inGame_PAISHAN.append(tmp)
    PAI_SHAN.remove(tmp)

#发牌(头14张)
mahjong = []
for i in range(0,14):
    mahjong.append(inGame_PAISHAN.pop())

def sort(assoc):
#手牌分区 => 帮助识别胡牌+帮助整理手牌
#分成 万子——索子——饼子——字牌(东南西北白发中) 四个区块
    manzi = []
    suozi = []
    binzi = []
    zipai = []

    #分成四块
    for i in range(0,len(assoc)):
        tmp = assoc[i]
        if tmp[1] == "m":
            manzi.append(tmp)
        elif tmp[1] == "s":
            suozi.append(tmp)
        elif tmp[1] == "p":
            binzi.append(tmp)
        else:
            zipai.append(tmp)

    #SORTING
    sort = [manzi,suozi,binzi,zipai]
    assoc = []
    for s in range(0,len(sort)):
        if sort[s] != zipai:
            for j in range(0,len(sort[s])-1):
                min = sort[s][j]
                idx = -1
                for i in range(j,len(sort[s])):
                    if min > str(sort[s][i]) and min:
                        min = sort[s][i]
                        idx = i
                if idx>0:
                    tmp = sort[s][j]
                    sort[s][j] = min
                    sort[s][idx] = tmp
        if sort[s] == zipai:
            temp = []
            model = ["Df","Nf","Xf","Bf","BB","FC","HZ"]
            while zipai:
                temp.append(zipai.pop())
            for i in range(0,len(model)):
                for j in range(0,temp.count(model[i])):
                    zipai.append(model[i])
    for i in range(0,len(sort)):
        for j in range(0,len(sort[i])):
            assoc.append(sort[i][j])
    return assoc

#检测胡牌
#测试手牌
mahjong = sort(mahjong)
print(mahjong)
mahjong = ['1m','1m','1m','2m','3m','4m','5m','5m','6m','7m','8m','9m','9m','9m']

#检查将眼
temp = []
JIANG_YAN = []
for i in range(0,len(mahjong)-1):
    if mahjong[i] == mahjong[i+1]:
        JIANG_YAN.append(mahjong[i])
#将眼去重
for i in range(0,len(JIANG_YAN)-1):
    if JIANG_YAN[i]==JIANG_YAN[i+1]:
        temp.append(JIANG_YAN[i])
for i in range(0,len(temp)):
    JIANG_YAN.remove(temp[i])

print(JIANG_YAN)

#七小对
if len(JIANG_YAN)>=7:
    HU = True

#常规胡种
SHUN_ZI = []
KE_ZI = []
temp = []
if JIANG_YAN:
    for i in range(0,len(JIANG_YAN)):
        #抽出将眼
        mahjong.remove(JIANG_YAN[i])
        mahjong.remove(JIANG_YAN[i])
        print(mahjong)
        #抽出刻子
        for j in range(0,len(mahjong)-2):
            if mahjong[j] == mahjong[j+1] and mahjong[j] == mahjong[j+2]:
                KE_ZI.append(mahjong.pop(j+2))
                KE_ZI.append(mahjong.pop(j+1))
                KE_ZI.append(mahjong.pop(j))
                print(KE_ZI)
                print(mahjong)
                


        mahjong.append(JIANG_YAN[i])
        mahjong.append(JIANG_YAN[i])
        mahjong = sort(mahjong)





