a = [int(x) for x in input().split()]
b = a[:]
b[0] = 5
for x in a:
    print(x,end = " ")
print("")
for x in b:
    print(x,end = " ")
# 输入用空格分隔的若干个整数
# 先将这些整数原样输出
# 然后将第一个整数改成5，其他不变，输出

# 输入样例:
# 1 2 3
# 输出样例：
# 1 2 3
# 5 2 3

print("")

lst1 = [6,7,8,9,0]
new_lst1 = lst1         #这里是引用赋值，lst1和new_lst1指向同一个东西
new_lst1[1] = 999
print(lst1)
print(new_lst1)

lst = [6,7,8,9,0]
new_lst = lst[:]        #这里是浅拷贝，除了嵌套列表里的元素的修改等，其他不可变数据类型互不影响
new_lst[1] = 999
print(lst)
print(new_lst)

lst2 = [[1,1,1],2,2,2]
new_lst2 = lst2
new_lst2[0][1] = 888
print(lst2)
print(new_lst2)

lst2 = [[1,1,1],2,2,2]
new_lst2 = lst2[:]
new_lst2[0][1] = 888
print(lst2)
print(new_lst2)


import copy
lst3 = [[1,1,1],2,2,2]
new_lst3 = copy.deepcopy(lst3)      #深拷贝，你我毫不相干
new_lst3[0][1] = 888
print(lst3)
print(new_lst3)