k = int(input())
ren_dict = {}
piao_dict = {}
ren_set = set()
piao_set = set()
for i in range(k):
    ren,piao,qian = input().split()
    qian = float(qian)
    if ren not in ren_dict:
        ren_dict[ren] = qian
    else:
        ren_dict[ren] += qian
    if piao not in piao_dict:
        piao_dict[piao] = qian
    else:
        piao_dict[piao] += qian
    ren_set.add(ren)
    piao_set.add(piao)
ren_list = sorted(ren_set)
piao_list = sorted(piao_set)

print(len(ren_list))
print(len(piao_list))
for ren in ren_list:
    print(f"{ren} {ren_dict[ren]:.2f}")
for piao in piao_list:
    print(f"{piao} {piao_dict[piao]:.2f}")

