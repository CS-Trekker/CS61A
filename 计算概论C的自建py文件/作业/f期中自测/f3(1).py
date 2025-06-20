n = int(input())

gifts = list(map(int,input().split()))

cnt_max_lst = []
for i in range(0,len(gifts)):
    for j in range(i,len(gifts)):
        if sum(gifts[i:j+1])%520 == 0:
            cnt_max = sum(gifts[i:j+1])
            cnt_max_lst.append(cnt_max)

print(cnt_max_lst)
if len(cnt_max_lst) != 0:
    print(max(cnt_max_lst))
else:
    print(0)