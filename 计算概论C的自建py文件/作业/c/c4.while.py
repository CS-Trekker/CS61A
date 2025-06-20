n = int(input())#输入n
a = 0#定义a为0
m = 1#从第1次开始
while m <= n:#当m小于等于n时
    m += 1#总次数加1
    b = int(input())#输入b
    a += b#a加上b
ava = "{:.5f}".format(a / n)#平均数,精确到小数点后5位
print(a,ava)#输出最后的和
