sentense = input()#输入字符串
count = 0#计数器
for _ in sentense:#遍历字符串
    if _ == '1' or _ == '2' or _ == '3' or _ == '4' or _ == '5' or _ == '6' or _ == '7' or _ == '8' or _ == '9' or _ == '0':#判断是否为数字
        count += 1#计数器加1
print(count)#输出计数器总数