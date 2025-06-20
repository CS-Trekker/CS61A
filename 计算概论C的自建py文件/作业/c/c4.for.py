n = int(input())#输入n
a = 0#初始化a
for i in range(n):#循环n次
    b = int(input())#输入b
    a += b#将b加到a上
ava = "{:.5f}".format(a / n) # 保留5位小数
print(a,ava)#输出a和平均值