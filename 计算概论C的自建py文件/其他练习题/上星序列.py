n = int(input())


shuyins_pais = []
pais = []
# shuyins = []
for i in range(n):
    shuyin,pai = input().split()
    shuyins_pais.append([shuyin,pai])
    pais.append(pai)
    # shuyins.append(shuyin)
xing_count = 0
for i in shuyins_pais:
    if i[0] == "Victory":
        if i[1] == "Gold":
            xing_count += 2
        elif i[1] == "Silver":
            xing_count += 1
        else:
            xing_count += 1
    else:
        if i[1] == "Gold":
            xing_count += 0
        elif i[1] == "Silver":
            xing_count -= 1
        else:
            xing_count -= 1
xing_count += (pais.count("Silver")//3)

print(xing_count)