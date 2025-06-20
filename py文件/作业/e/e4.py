m = int(input())#输入一个整数m
dict = {}#创建一个空字典
for i in range(m):#循环m次
    a,b = input().split()#输入两个字符串
    dict[a] = b#将a作为键，b作为值存入字典
sen = input()#输入一个字符串
for i in range(len(sen)):#循环字符串的长度次
    print(dict.get(sen[i]),end = "")

#在print函数里写end = ""表示不换行