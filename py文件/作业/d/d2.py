n = int(input())#输入n
A,B,C = 0,0,0#初始化A,B,C
for i in range(n):#循环n次
    a,b,c = map(int,input().split())#输入a,b,c
    A += a#金牌
    B += b#银牌
    C += c#铜牌
print(A,B,C,A+B+C)#输出金银铜牌总数和奖牌总数