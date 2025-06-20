n = int(input())

show_lst = []
for i in range(n):
    show = {}
    show_name, actor, mark, review_num = input().split()
    review_num = int(review_num)
    mark = float(mark)
    if review_num < 100:
        continue
    if mark < 9.0:
        continue
    if "," in actor:
        actors = actor.split(",")
    else:
        actors = [actor]
    show[show_name] = actors
    show_lst.append(show)

# print(show_lst)
# [{'独舞《春》': ['liling']},
# {'双人舞《青春的起点》': ['liling', 'wanghui']}]

# 记录演员的表现
actors = {}

for show in show_lst:
    # print(show)
    # {'独舞《春》': ['liling']}
    # print(show.values())
    # dict_values([['liling']])
    for actors_list in show.values():
        # print(actors_list)
        # ['liling']

        # 对演员名单排序
        sorted_actors = sorted(actors_list)

        for actor in sorted_actors:
            if actor not in actors:
                actors[actor] = {"count": 0, "shows": []}
            actors[actor]["count"] += 1 / len(sorted_actors)  # 根据演员数量给予不同的权重
            actors[actor]["shows"].append(list(show.keys())[0])  # 将节目的名称添加到演员的shows列表

# print(actors)
# {'liling': {'count': 1.5, 'shows': ['独舞《春》', '双人舞《青春的起点》']},
# 'wanghui': {'count': 0.5, 'shows': ['双人舞《青春的起点》']}}

# 按演员名字的字母序输出
for actor in sorted(actors.keys()):  # 对演员名字进行字母序排序
    data = actors[actor]
    # 输出演员名字、总评分（保留一位小数）、参与的节目，节目之间用空格分隔
    print(f"{actor} {data['count']:.1f} {' '.join(data['shows'])}")