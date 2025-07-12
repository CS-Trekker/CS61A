import re
stri = input()
lst = re.findall(r"[aeiou]{2,}",stri)
print(*lst)