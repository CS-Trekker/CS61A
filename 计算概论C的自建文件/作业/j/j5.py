def visit_time(start,end):
    hour,minute,second = map(int,start.split(":"))
    start_second = hour*3600 + minute*60 + second
    hour,minute,second = map(int,end.split(":"))
    end_second = hour * 3600 + minute * 60 + second
    times = end_second - start_second
    return times


n = int(input())
dic = {}
for i in range(n):
    web,start,end = input().split()
    # print(visit_time(start,end))
    dic[web] = dic.get(web,0) + visit_time(start,end)
max_web = max(dic,key = dic.get)
print(max_web)
