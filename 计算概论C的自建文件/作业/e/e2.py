n,k = map(int,input().split())#输入n和k
lst = list(map(int,input().split()))#输入n个数字
flag = "no"#初始化flag
for i in range(n):#遍历列表
    for j in range(i+1,n):#遍历列表
        if lst[i]+lst[j] == k:#判断两个数之和是否等于k
            flag = "yes"#如果等于k，则flag为yes
            break#跳出循环
        if flag == "yes":#如果flag为yes，则跳出循环
            break#跳出循环
print(flag)#输出flag
        
