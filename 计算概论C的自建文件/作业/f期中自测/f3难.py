n = int(input())
lst = list(map(int,input().split()))

max_sum = 0
for i in range(n-1):
    now_sum = lst[i]
    for j in range(i+1,n):
        now_sum += lst[j]
        if now_sum % 520 == 0:
            max_sum = max(now_sum,max_sum)
max_sum = max(max_sum,lst[n-1])

print(max_sum)