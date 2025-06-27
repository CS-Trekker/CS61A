def reverse(s:str):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]