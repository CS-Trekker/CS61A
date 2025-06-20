def changeme(x):
    x = 10

a = 2
changeme(a)
print(a)
#结果是2


def change(mylist):
    mylist.append(40)

lst1 = [10,20,30]
change(lst1)
print(lst1)
#结果是[10, 20, 30, 40]


#不可变数据类型:数字，字符串，元组
#可变数据类型 :列表，字典，集合

def reassign(lst):
    lst[0] = 3
    lst = [2, 2, 2]
    lst[0] = 4
    print("函数输出的lst:", lst)

lst = [1, 1, 1]
reassign(lst)
print("函数外面的lst:",lst)



def g(n):
    n = 999
    print("函数输出的n或m:",n)
n = 1
g(n)
print("函数外面的n:",n)

m = 2
g(m)
print("函数外面的m:",m)