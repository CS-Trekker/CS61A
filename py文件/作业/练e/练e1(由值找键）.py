letterBook = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--.."}

shu_ru = input()
if shu_ru.isalpha():
    lst = []
    for i in shu_ru:
        i = i.upper()
        lst.append(i)
    # print(lst)
    # ['C', 'O', 'U', 'N', 'T', 'S']
    done_lst = []
    for i in lst:
        i = letterBook[i]
        done_lst.append(i)
    print(*done_lst,sep="/")
else:
    moles_lst = shu_ru.split("/")
    # print(moles_lst)
    # ['.-.', '.', '...', '..', '...', '-', '.-', '-.', '-.-.', '.', '...']
    for i in moles_lst:
        for key,value in letterBook.items():
            if i == value:
                print(key,end="")