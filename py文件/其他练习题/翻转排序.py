n = int(input())
reversed_i_list = []
for i in range(1,n+1):
    str_i = str(i)
    str_i_list = []
    for j in str_i:
        str_i_list.append(j)
    str_i_list.reverse()
# print(str_i_list)
# ['3', '2', '1']
    reversed_i = int("".join(str_i_list))
    # print(reversed_i)
    reversed_i_list.append([i,reversed_i])
reversed_i_list.sort(key=lambda x:(-x[1],x[0]))
for i in reversed_i_list:
    print(i[0],end=" ")