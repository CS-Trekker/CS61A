n = int(input())

lst = []
for i in range(n):
    name,mark = input().split()
    mark = int(mark)
    stu = {}
    stu["name"] = name
    stu["mark"] = mark
    lst.append(stu)
# print(lst)

new_lst = sorted(lst,key = lambda n : (-n["mark"],n["name"]))
# print(new_lst)
for stu in new_lst:
    print(stu["name"],stu["mark"])