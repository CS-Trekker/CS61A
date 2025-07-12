def total(n) :
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return total(n-1) + total(n-2)
n = int(input())
print(total(n))