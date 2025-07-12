# import re
#
# n = int(input())
# for i in range(n):
#     stri = input()
#     lst = re.findall(r"<(\d{1,3}?)>",stri)
#     # new_lst = []
#     if len(lst) != 0:
#         new_lst = [i for i in lst if (not i.startswith("0")) or i == "0"]
#         # for i in lst:
#         #     if (not i.startswith("0")) or i == "0":
#         #         new_lst.append(i)
#         print(*new_lst)
#     else:
#         print("NONE")
##### 以下为最简写法 #####


import re

n = int(input())
for i in range(n):
    stri = input()
    lst = re.findall(r"<([1-9]\d{0,2}|0)>",stri)
    if len(lst) != 0:
        print(*lst)
    else:
        print("NONE")