s="aiassafaaaafva"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])

i = int(input())
[s[i:j] for i in range(len(s)) for j in range(i + 1,len(s) + 1)]