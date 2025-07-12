s = input()
flag = False
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            flag = True
            break
        if flag:#任何字符都有逻辑值
            break
if flag:
    print("Yes")
else:
    print("No")


    