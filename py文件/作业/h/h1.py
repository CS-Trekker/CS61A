def gcd(a,b):
    if a < b:
        a,b = b,a
    while True:
        if a % b != 0:
            a,b = b,(a % b)
        else :
            c = b
            return c
a, b = map(int, input().split())
print(gcd(a, b))