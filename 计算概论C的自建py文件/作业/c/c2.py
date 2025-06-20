a,b,c,d=input().split()#输入
b,d=int(b),int(d)#将b,d转化为整数
if a=="M":#如果a是男
    if b>=22 and d>=20:#如果男不早于22岁，女不早于20岁
        print("legal")#合法
    else:#否则
        print("illegal")#不合法
else:#如果a是女
    if b>=20 and d>=22:#如果女不早于20岁，男不早于22岁
        print("legal")#合法
    else:#否则
        print("illegal")#不合法