#胡豪 大作业 12月4日

text = open("The_Red_Headed_League.txt","r",encoding = "utf-8")

dic = {}
while True:
    try:
        line = text.readline()
        if line == "":
            break
        else:
            lst = list(line.split())
            for i in lst:
                i = i.strip(",").strip(".").lower()
                dic[i] = dic.get(i,0) + 1#统计词频专用
            # print(dic)
    except:
        break
text.close()

words = list(dic.keys())
words.sort(key = lambda n : (-dic[n],n))
new_file = open("Holmes_Word_Count.txt","w",encoding = "utf-8")
for word in words:
    # print(word,dic[word])
    new_file.write(word+" "+str(dic[word])+"\n")
new_file.close()