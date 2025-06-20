n = int(input())

word_sheet = {}


location = 0
for i in range(n):
    word = input()
    if word not in word_sheet:
        word_sheet[word] = []
    word_sheet[word].append(location)
    location += 1
# print(word_sheet)
# {'Carol': [0, 5], 'Alice': [1, 4, 6], 'Bob': [2, 3]}

for i in sorted(word_sheet.keys()):
    # print(i)
    shuchu = [word_sheet[i][0]]
    for j in range(1,len(word_sheet[i])):
        # print(word_sheet[i][j])#4，6
        word_sheet[i][j] -= word_sheet[i][j-1]
        shuchu.append(word_sheet[i][j])
        word_sheet[i][j] += word_sheet[i][j - 1]
    # print(shuchu)
    # [1, 3, 2]
    print(i,":",*shuchu)