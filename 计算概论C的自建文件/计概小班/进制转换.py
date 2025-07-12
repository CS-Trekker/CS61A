#把十进制的n转换成m进制的数
def trans(n,m) :
    if n == 0:
        return ""
    return trans(n // m,m) + str(n % m)
a,k = map(int,input().split())
print(trans(a,k))

