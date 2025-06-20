N,M = map(int,input().split())#输入N和M

flag = -1#初始化flag

for a in range(1,N+1):#遍历1到N
    if N%a==0 and M-a > 0 and N %(M-a)==0:#如果N能被a整除且M-a大于0且N能被M-a整除
        flag = a#将a赋值给flag
        break#跳出循环
print(flag)#输出flag
#1是任何非零整数的因子