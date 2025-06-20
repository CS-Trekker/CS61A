n,m = map(int,input().split())

xinmins = []
for i in range(n):
    xinmin = input()
    xinmins.append(xinmin)

fuxins = []
for i in range(m):
    fuxin = input()
    fuxins.append(fuxin)

# print(xinmins,fuxins)
# ['陈刚', '王兵', '欧阳滨', '王国军', '姜明', '欧阳东明'] ['欧阳', '上官']

xins = []
xins_num = {}
for xinmin in xinmins:
        if xinmin[:2] in fuxins and len(xinmin) > 2:
            xins.append(xinmin[:2])
            xins_num[xinmin[:2]] = xins_num.get(xinmin[:2],0) + 1
        else:
            xins.append(xinmin[0])
            xins_num[xinmin[0]] = xins_num.get(xinmin[0],0) + 1

xins = sorted(list(set(xins)),key=lambda x:(-xins_num[x],x))
# print(xins)

for xin in xins:
    print(xin,xins_num[xin])