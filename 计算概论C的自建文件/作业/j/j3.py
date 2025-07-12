# 大写字母A-Z的ASCII码范围是65到90
# 小写字母a-z的ASCII码范围是97到122


n = int(input())
i = input()
if i == "E":
    ming = input()
    ming_lst = [i for i in ming]
    # print(ming_lst)
    mima_lst = []
    for i in ming_lst:
        if "A" <= i <= "Z":     # if 65 <= ord(i) <= 90:
            i = chr((ord(i)- 65 + n) % 26 + 65)
            mima_lst.append(i)
        elif "a" <= i <= "z":       #97 <= ord(i) <= 122
            i = chr((ord(i)- 97 + n) % 26 + 97)
            mima_lst.append(i)
        else:
            mima_lst.append(i)
    print(*mima_lst,sep = "")

if i == "D":
    mima = input()
    mima_lst = [i for i in mima]
    ming_lst = []
    for i in mima_lst:
        if "A" <= i <= "Z":  # if 65 <= ord(i) <= 90:
            i = chr((ord(i) - 65 - n) % 26 + 65)
            ming_lst.append(i)
        elif "a" <= i <= "z":  # 97 <= ord(i) <= 122
            i = chr((ord(i) - 97 - n) % 26 + 97)
            ming_lst.append(i)
        else:
            ming_lst.append(i)
    print(*ming_lst, sep="")