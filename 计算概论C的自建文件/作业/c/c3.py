a=input()#输入
b=a[:-2:-1]#取最后一位
if b=="F":#判断是否为华氏度
    a=float(a.strip("F"))#去掉F
    c=(a-32)*(5/9)#计算
    print("%.2f"%c+"C")#输出摄氏度
else:#否则
    a=float(a.strip("K"))#去掉K
    c=a+273.15#计算
    print("%.2f"%c+"C")#输出摄氏度
    
    