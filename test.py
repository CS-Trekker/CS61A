try:
    x = 1/0
except ZeroDivisionError as e:
    print(type(e))
    x = 0