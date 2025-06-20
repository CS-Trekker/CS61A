#filter函数:
def is_odd(n):
    return n % 2 == 1
lst = [1,2,3,4,5,6,7,8]
new_lst = filter(is_odd,lst)
# print(type(new_lst)) 得到的是 filter数据类型，不是 列表
print(list(new_lst))

#匿名函数:
orilist = [1,2,3,4,5,6,7,8]
newlist = filter(lambda n: n % 2 == 1, orilist)#lambda后面的n不要括号
print(list(newlist))

lst = [(1,4),(3,2),(2,2),(4,3)]
lst.sort(key = lambda x : x[1],reverse = True)#x代表的是(1,4)、(3,2)这些东西
print(lst)

#多关键字排序
L = [("摩洛哥",2,2,0,1),("葡萄牙",5,4,1,5),("西班牙",6,5,1,5),("伊朗",2,2,0,4)]#进球，失球，净胜球，积分
new_L = sorted(L, key = lambda x: (x[4],-x[2],x[1]),reverse = True)
print(new_L)

new_L1 = sorted(L,key = lambda x: (-x[2],x[3],x[4],x[1]),reverse = True)
print(new_L1)

