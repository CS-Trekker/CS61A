n = int(input())
qian_dao_dict = {}
for i in range(n):
    id,date = input().split()
    qian_dao_dict[id] = qian_dao_dict.get(id,set())
    qian_dao_dict[id].add(date)
for i in sorted(qian_dao_dict.keys(),key=lambda x:(-len(qian_dao_dict[x]),x)):
    print(i,len(qian_dao_dict[i]))
