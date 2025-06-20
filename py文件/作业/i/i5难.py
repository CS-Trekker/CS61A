n = int(input())
dates = {}
for i in range(n):
    name,mon,day = input().split()
    mon = int(mon)
    day = int(day)
    date = tuple([mon,day])
    current_dates = list(dates.keys())
    if date not in current_dates:
        dates[date] = [name]
    else:
        dates[date].append(name)
# print(dates)

#输出结果部分：

#删除不是同一天生日的生日
#如果没有则输出None
dateskeys = list(dates.keys())
for i in dateskeys:
    if len(dates[i]) < 2:
        del dates[i]
# print(dates)
if len(dates) == 0:
    print("None")

#先进行日期排序
new_dateskeys = list(dates.keys())
new_dateskeys.sort(key = lambda n : (n[0],n[1]))
# print(new_dateskeys)

#再进行名字排序
for i in new_dateskeys:
    dates[i].sort(key = lambda x : (len(x),x))
# print(dates)

for i in new_dateskeys:
    print(*i,*dates[i])