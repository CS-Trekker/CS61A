sentense = input()#输入字符串
count=0#计数器
for i in sentense:# 遍历字符串
    if i.isdigit():#判断是否为数字
        count+=1#计数器加1
print(count)#输出计数器总数