dict = {}#创建一个空字典
while True:#循环
    n = input()#输入
    if n[0] == "a":#如果输入的第1个字符是a
        a,name,loc = n.split()#将输入的字符串以空格为分隔符，分成三个部分
        dict[name] = loc#将name作为键，loc作为值，存入字典
    elif n[0] == "q":#如果输入的第1个字符是q
        q,name = n.split()#将输入的字符串以空格为分隔符，分成两个部分
        if name in dict:#如果name在字典中
            print(dict[name])#输出name对应的值
        else:#如果name不在字典中
            print("Not found!")#输出Not found!
    elif n[0] == "e":#如果输入的第1个字符是e
        break#跳出循环