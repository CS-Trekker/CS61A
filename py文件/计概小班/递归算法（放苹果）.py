#把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？注意：5，1，1和1，5，1是同一种分法
def f(m,n):#“要相信”定义的这个函数能解决这个问题
    if m == 0 or n == 1:
        return 1
    elif m < n:
        return f(m,m)
    elif m >= n:
        return f(m-n,n)+f(m,n-1)#每个盘子里都有苹果+有盘子没有苹果

m,n = map(int,input().split())
print(f(m,n))