s = input().strip(".")#去掉末尾的.
lst = list(s.split())#以空格为分隔符，将字符串分割成列表
a = lst[0]#将列表的第一个元素赋值给a
for i in range(1,len(lst)):#从列表的第二个元素开始遍历
    if len(a) < len(lst[i]):#如果a的长度小于lst[i]的长度
        a = lst[i]#将lst[i]赋值给a
print(a)#输出a