a,b,c = input().split()#输入两个数和一个运算符
if c == "/" and b == "0":#除数不能为零
    print("Divided by zero!")#除数不能为零
elif c != "/" and c != "*" and c != "+" and c != "-":#  运算符只能为+ - * /
    print("Invalid operator!")#     运算符只能为+ - * /
elif c == "+":# 加法
    print(int(a) + int(b))#     输出结果
elif c == "-":#减法                                  
    print(int(a) - int(b))#    输出结果
elif c == "*":# 乘法
    print(int(a) * int(b))# 输出结果
elif c == "/":# 除法
    print(int(a) // int(b))# 输出结果