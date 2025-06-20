id = "21001220001001010x"

import re

lst1 = re.findall("a.*b","aababababab")#贪婪匹配
lst2 = re.findall("a.*?b","aababababab")#最小匹配
lst3 = lst = re.findall("a(.*?)b","aabaebafbagbah什么鬼b")#括号里面的表示捕获组
print(lst1)
print(lst2)
print(lst3)



m = re.match("py.","python")
if m:
    print("匹配")
else:
    print("不匹配")

m = re.match("py.$","python")
if m:
    print("匹配")
else:
    print("不匹配")



n = re.search("a","jianndsi")
if n:
    print("匹配")
else:
    print("不匹配")

n = re.search("^a","jianndsi")
if n:
    print("匹配")
else:
    print("不匹配")
