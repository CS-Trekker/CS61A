N = int(input())

ACs = []
for i in range(N):
    id,time,status,code_id = input().split()
    time = int(time)
    if status == "AC":
        ACer = [id,time,code_id]
        ACs.append(ACer)
ACs = sorted(ACs,key=lambda x:x[1])
# print(ACs)
# [['user5', 55, 'code2'], ['user3', 60, 'code2'], ['user1', 30, 'code3'], ['user4', 70, 'code2'], ['user2', 50, 'code3'], ['user6', 100, 'code4']]


cheat_code_lst = []
for i in range(0,len(ACs)):
    for j in range(i+1,len(ACs)):
        # cheaters = {}

        if ACs[i][2] == ACs[j][2]:
            cheat_code_lst.append(ACs[i][2])
# print(cheat_code_lst)
cheat_codes = sorted(list(set(cheat_code_lst)))

# print(cheat_codes)
# ['code2', 'code3']

for i in cheat_codes:
    lst = []
    for k in ACs:
        if k[2] == i:
            lst.append(k[0])
    # print(lst)
    # ['user5', 'user3', 'user4']
    # ['user1', 'user2']
    print(i,len(lst),*lst)
