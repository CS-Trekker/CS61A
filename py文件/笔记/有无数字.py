s = input()

flag=False

for i in range(len(s)):
    if s[i] <= "9" and s[i] >= "0":
        flag=True
        break #避免超时

if flag:
    print("yes")
else:
    print("no")