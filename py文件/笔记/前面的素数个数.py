m = int(input())

count = 0

for i in range(2,m+1):
    flag = True
    import math
    a = int(i ** 0.5) + 1       #两种情况:若i是完全平方数，则(2，a)表示从2到根号i;若i不是完全平方数，则(2,a)表示从2到根号i的下取整
    b = math.ceil(i ** 0.5)     #b是错误的，如果使用b，则会将4、9、25、49也误认为是素数
    c = math.floor(i ** 0.5)    #c也是错误的,则会有更多误判为素数
    for j in range(2,a):
        if i%j==0:
            flag = False
            break
    if flag:
        count += 1
        print(i)
print(count)