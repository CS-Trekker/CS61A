def total(x):
    if x == 1:
        return 1
    else:
        return (total(x-1)+1)*2

m = int(input())
for i in range(m):
    n = int(input())
    print(total(n))
