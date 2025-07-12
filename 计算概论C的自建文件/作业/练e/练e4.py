n,m = map(int,input().split())
menu = {}
for i in range(m):
    cai,qian,liang = input().split()
    qian = int(qian)
    liang = int(liang)
    menu[cai] = [qian,liang]
# print(menu)

sum = 0
current = {}
for i in range(n):
    lst = input().split()
    for i in lst:
        current[i] = current.get(i,0) + 1
        if current[i] <= menu[i][1]:
            sum += menu[i][0]
    # for k in current:
    #     print(k,current[k])

print(sum)