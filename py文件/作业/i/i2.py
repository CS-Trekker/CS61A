N = int(input())
set1 = set()
lst1 = list(map(int,input().split()))
# print(lst1)

for i in lst1:
    set1.add(i)
# print(set1)

lst2 = list(set1)
lst2.sort()

print(len(lst2))
print(*lst2)