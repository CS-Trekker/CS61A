s = input()#输入字符串

flag = "no"#初始化标记

for i in range(len(s)):#遍历字符串
    if s.count(s[i]) == 1:#如果字符串中只有一个字符
        flag = s[i]#标记为该字符
        break#跳出循环
print(flag)#输出标记