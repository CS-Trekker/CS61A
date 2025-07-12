squares = [ x**2 for x in range (10)]
print(squares)

#列表生成式
a = [i for i in range(10,30,5)]
print(a)

b = [[x,y] for x in [1,2,3] for y in [4,5,6] if x != y]#列表生成式
print(b)