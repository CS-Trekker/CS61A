summary = [0 for i in range(51)]
for i in range(10):
    num = int(input())
    summary[num] += 1
for i in range(51):
    print("数字%d有%d个"%(i,summary[i]))