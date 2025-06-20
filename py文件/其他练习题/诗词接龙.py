score = {}
N = int(input())
last_zi_yin = None
last_zi_diao = None
for i in range(N):
    name, words = input().split(":")
    if name not in score:
        score[name] = 0
    huida = words.split(" ")
    first_zi = huida[0]

    first_zi_yin = first_zi[:-1]
    first_zi_diao = first_zi[-1]

    if first_zi_yin == last_zi_yin:
        if first_zi_diao == last_zi_diao:
            score[name] += 2
        else:
            score[name] += 1
        last_zi = huida[-1]
        last_zi_yin = last_zi[:-1]
        last_zi_diao = last_zi[-1]
    if not last_zi_yin:
        last_zi = huida[-1]
        last_zi_yin = last_zi[:-1]
        last_zi_diao = last_zi[-1]
for name, score in sorted(score.items(), key=lambda x:(-x[1], x[0])):
    print(name, score)


# N = int(input())
#
# huida_lst = []
# for i in range(N):
#     huida = input().split()
#     name,first_zi = huida[0].split(":")
#
#     first_zi_yin = first_zi[:len(first_zi)-1]
#     first_zi_diao = first_zi[-1]
#
#     last_zi = huida[-1]
#     last_zi_yin = last_zi[:len(last_zi)-1]
#     last_zi_diao = last_zi[-1]
#
#     huida_lst.append([name,first_zi_yin,first_zi_diao,last_zi_yin,last_zi_diao])
#
# # print(huida_lst)
# # [['Dongzhu', 'chun', '1', 'ping', '2'], ['Alice', 'ping', '2', 'yu', '3'], ['Bob', 'ping', '2', 'yu', '3'], ['Alice', 'ha', '1', 'la', '0'], ['Carol', 'yu', '2', 'jian', '1'], ['Dongzhu', 'jian', '1', 'hua', '2'], ['Dave', 'hua', '1', 'shao', '3'], ['Alice', 'shao', '4', 'li', '4'], ['Dongzhu', 'li', '4', 'ku', '3'], ['Dave', 'ku', '1', 'bi', '4']]
# names = sorted(list(set([x[0] for x in huida_lst])))
# # print(names)
# # ['Alice', 'Bob', 'Carol', 'Dave', 'Dongzhu']
#
# current_last_yin = huida_lst[0][3]
# current_last_diao = huida_lst[0][4]
# del huida_lst[0]
# # print(huida_lst)
# # [['Alice', 'ping', '2', 'yu', '3'], ['Bob', 'ping', '2', 'yu', '3'], ['Alice', 'ha', '1', 'la', '0'], ['Carol', 'yu', '2', 'jian', '1'], ['Dongzhu', 'jian', '1', 'hua', '2'], ['Dave', 'hua', '1', 'shao', '3'], ['Alice', 'shao', '4', 'li', '4'], ['Dongzhu', 'li', '4', 'ku', '3'], ['Dave', 'ku', '1', 'bi', '4']]
# # print(current_last_yin)#ping
# # print(current_last_diao)#2
# mark = {}
#
# for i in huida_lst:
#     if i[1] == current_last_yin:
#         if i[2] == current_last_diao:
#             mark[i[0]] = mark.get(i[0],0) + 2
#         else:
#             mark[i[0]] = mark.get(i[0], 0) + 1
#         current_last_yin = i[3]
#         current_last_diao = i[4]
#
# # print(mark)
# # {'Alice': 3, 'Carol': 1, 'Dongzhu': 4, 'Dave': 2}
#
# names.sort(key=lambda x:(-mark.get(x,0),x))
# # print(names)
# # ['Dongzhu', 'Alice', 'Dave', 'Carol', 'Bob']
#
# for i in names:
#     print(i,mark.get(i,0))