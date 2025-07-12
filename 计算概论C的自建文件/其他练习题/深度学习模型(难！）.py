n = int(input())

moxinnames = []
canshuliangs = {}
teams = {}
dates = {}
fields = {}

for i in range(n):
    moxinname, canshuliang, team, year, month, day, application = input().split("-")
    if "," in application:
        application = list(application.split(","))
    else:
        application = [application]

    if moxinname not in moxinnames:
        canshuliangs[moxinname] = []
        teams[moxinname] = set()
        dates[moxinname] = []
        fields[moxinname] = set()

    # 参数量加入列表
    if canshuliang[-1] == "M":
        value = int(canshuliang[:-1])
    elif canshuliang[-1] == "B":
        value = int(float(canshuliang[:-1]) * 1000)
    canshuliangs[moxinname].append((value, canshuliang))  # 添加数值和原始字符串

    # 开发团队
    teams[moxinname].add(team)

    # 开发时间
    dates[moxinname].append([year, month, day])

    # 应用领域
    for app in application:
        fields[moxinname].add(app)

    moxinnames.append(moxinname)

# 去重并按字典序排序
moxinnames = sorted(list(set(moxinnames)))

# 构建输出
for moxinname in moxinnames:
    # 参数量排序
    sorted_canshuliangs = sorted(canshuliangs[moxinname], key=lambda x: x[0])
    sorted_canshuliangs_str = ",".join(x[1] for x in sorted_canshuliangs)

    # 开发团队数量
    team_num = len(teams[moxinname])

    # 最早开发时间
    dates[moxinname].sort(key=lambda x: (x[0], x[1], x[2]))
    earliest_date = "-".join(dates[moxinname][0])

    # 应用领域数量
    application_num = len(fields[moxinname])

    # 输出
    print(f"{moxinname}:{sorted_canshuliangs_str}/team:{team_num}/date:{earliest_date}/application:{application_num}")