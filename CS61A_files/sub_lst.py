def sub_lst(lst):
    if lst == []:
        return [[]]
    else:
        rest_subs = sub_lst(lst[1:])
        first = lst[0]
        return rest_subs + [[first] + ls for ls in rest_subs]