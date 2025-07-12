def ph(x,memo=[0,1,1]):
    if x <= len(memo)-1:
        return memo[x]
    else:
        memo.append(ph(x - 1) + ph(x - 2))
        return ph(x-1) + ph(x-2)

x = int(input())
print(ph(x))