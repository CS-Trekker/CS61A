n = int(input())

mark_sheet = {} #mark_sheet里面的键是课程，值是字典（学生为键，成绩为值）

for i in range(n):
    lesson,name,mark = input().split()
    mark = int(mark)
    if lesson not in mark_sheet:
        mark_sheet[lesson] = {}
    mark_sheet[lesson][name] = mark

# print(mark_sheet)
# {'JiSuanGaiLunA': {'XiaoWang': 100, 'XiaoZhang': 98, 'XiaoHong': 95},
# 'GaoDengShuXue': {'XiaoHong': 95, 'XiaoZhang': 84, 'XiaoWang': 82, 'XiaoHuang': 88},
# 'MeiRenLiJieJiSuanJiXiTong': {'XiaoWang': 82, 'XiaoZhang': 84, 'XiaoHong': 99, 'XiaoDuan': 100},
# 'PythonCongRuMengDaoFangQi': {'HYL': 100, 'SWE': 98, 'CDW': 95, 'ASC': 92, 'DEF': 90},
# 'GuHanYu': {'HYL': 95, 'ASC': 90, 'CDW': 86},
# 'CollegeEnglish': {'SWE': 82, 'CDW': 85, 'DEF': 82}}

m = int(input())

groups = []
for i in range(m):
    lesson_group = list(input().split())
    lesson_group[0] = int(lesson_group[0])
    groups.append(lesson_group)
# print(groups)
# [[3, 'JiSuanGaiLunA', 'GaoDengShuXue', 'MeiRenLiJieJiSuanJiXiTong'], [2, 'PythonCongRuMengDaoFangQi', 'GuHanYu'], [2, 'PythonCongRuMengDaoFangQi', 'CollegeEnglish']]

for i in groups:
    same_stu = set(mark_sheet[i[1]])
    k = i[0]
    for j in range(2,k+1):
        same_stu = same_stu & set(mark_sheet[i[j]].keys())
    # print(same_stu)
    # {'XiaoHong', 'XiaoZhang', 'XiaoWang'}
    # {'CDW', 'ASC', 'HYL'}
    # {'CDW', 'DEF', 'SWE'}

    juanwang_sheet = {}

    #注意i是列表

    i.pop(0)
    # print(i)
    # ['JiSuanGaiLunA', 'GaoDengShuXue', 'MeiRenLiJieJiSuanJiXiTong']
    for p in i:
        for q in same_stu:
            if q not in juanwang_sheet:
                juanwang_sheet[q] = []
            juanwang_sheet[q].append(mark_sheet[p][q])
    # print(juanwang_sheet)
    # {'XiaoHong': [95, 95, 99], 'XiaoWang': [100, 82, 82], 'XiaoZhang': [98, 84, 84]}

    for i in juanwang_sheet.keys():
        juanwang_sheet[i] = sum(juanwang_sheet[i])
    # print(juanwang_sheet)
    # {'DEF': 172, 'SWE': 180, 'CDW': 180}

    lst = list(juanwang_sheet.keys())
    lst.sort(key = lambda x:(-juanwang_sheet[x],x))
    print(lst[0])