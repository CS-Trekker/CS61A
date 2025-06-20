n = int(input())
old_lst = []
young_lst = []
for i in range(n):
    ID , age = input().split()
    age = int(age)
    dic = {}
    dic["ID"] = ID
    dic["age"] = age
    if age >= 60:
        old_lst.append(dic)
    else:
        young_lst.append(dic)
# print(old_lst)
# print(young_lst)

old_lst.sort(key = lambda n: n["age"],reverse = True)
for i in old_lst:
    print(i["ID"])
for i in young_lst:
    print(i["ID"])