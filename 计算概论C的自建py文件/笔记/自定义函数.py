def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
#调用函数
a,b,c = map(int,input().split())
print(area(a,b,c))

def f(a,b):
    return a+b
a = 1
b = 2
print(f(a,b))
