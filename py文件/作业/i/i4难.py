yuans = []
dic = {}
while True:
    inputs = input()
    if inputs.lower() == "quit":
        break
    try:
        xuehao,mark = inputs.split(",")
        mark = float(mark)
        # print(xuehao)
        # print(mark)
        yuan = xuehao[5:7]
        # print(yuan)
        if yuan not in yuans:
            yuans.append(yuan)
            dic[yuan] = [mark]
        else:
            dic[yuan].append(mark)
        # print(yuans)
    except:
        break

all = []
for i in yuans:
    ave = round(sum(dic[i]) / len(dic[i]) , 1)
    all.append([i,ave])
    # print(all)
all.sort(key = lambda x: x[1],reverse = True)
for i in all:
    print(i[0],i[1],sep = ",")