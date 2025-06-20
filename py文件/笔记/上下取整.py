import math

# ceil是向上取整
print(math.ceil(3.2))     # 输出：4
print(math.ceil(-3.8))    # 输出：-3
print(math.ceil(4.0))     # 输出：4

#与int函数的区别
print(math.ceil(100.5))   # 输出：101
print(int(100.5))         # 输出：100


# floor是向下取整
print(math.floor(3.7))    # 输出：3
print(math.floor(-3.2))   # 输出：-4
print(math.floor(5.0))    # 输出：5

#与int函数的区别
print(math.floor(-100.5)) # 输出：-101
print(int(-100.5))        # 输出：-100