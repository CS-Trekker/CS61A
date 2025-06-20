n = int(input())#输入一个正整数n
count = 0#计数器
for a in range(3,n+1):#遍历所有可能的a值
    for b in range(a,n+1):#遍历所有可能的b值
        if (a**2 + b**2)**0.5 == int((a**2 + b**2)**0.5) and (a**2 + b**2)**0.5 <= n:#判断是否满足条件
             count += 1#满足则计数器加1
print(count)#输出结果
#如果用三重循环将会超时