a=int(input())#输入一个整数
print(a//100)#输出100的张数
print(a%100//50)#输出50的张数
print(a%100%50//20)#输出20的张数
print(a%100%50%20//10)#输出10的张数
print(a%100%50%20%10//5)#输出5的张数
print(a%100%50%20%10%5)#输出1的张数