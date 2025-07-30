def edit_distance(origin: str, result: str):
    '''返回从origin通过增添、删除、修改三种操作变成result所需的最少操作次数。
    
    >>> edit_distance("abc", "abc")
    0
    >>> edit_distance("b", "abc")
    2
    >>> edit_distance("abcdef", "abadaf")
    2
    >>> edit_distance("abcdef", "abcf")
    2
    ''' 
    if origin == "":
        return len(result)
    elif result == "":
        return len(origin)
    elif origin == result:
        return 0
    elif origin[0] == result[0]:
        return edit_distance(origin[1:], result[1:])
    else:
        # add
        add_cost = 1 + edit_distance(origin, result[1:])
        # delete
        delete_cost = 1 + edit_distance(origin[1:], result)
        # revise
        revise_cost = 1 + edit_distance(origin[1:], result[1:])
        return min(add_cost, delete_cost, revise_cost)
    
# 但是效率很低
        

