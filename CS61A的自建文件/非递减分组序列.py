def nondecreaselist(lst):
    if not lst:  # 空列表
        return []
    if len(lst) == 1:  # 只有一个元素时，直接返回 [[元素]]
        return [[lst[0]]]

    # 从第一个元素开始，构造当前的 non-decreasing 子列表
    current = [lst[0]]
    i = 1
    while i < len(lst) and lst[i] >= lst[i-1]:
        current.append(lst[i])
        i += 1

    # 剩下的部分用递归继续处理
    return [current] + nondecreaselist(lst[i:])


print(nondecreaselist([1,2,3,4,1,2,3,4,1,1,1,2,1,1,0,4,3,2,1]))
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 1, 1, 2], [1, 1], [0, 4], [3], [2], [1]]