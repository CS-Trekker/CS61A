n = int(input())#输入n
a = list(map(int,input().split()))#输入列表a
b = list(map(int,input().split()))#输入列表b
c = 0#初始化c
for i in range(n):#遍历列表a
    c += a[i]*b[i]#计算a[i]*b[i]并累加到c
print(c)#输出c