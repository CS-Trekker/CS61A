str = "Hello World, Hello Python"

# 基本查找
print(str.find("Hello"))        # 输出：0（第一个Hello的位置）
print(str.find("World"))        # 输出：6
print(str.find("Java"))         # 输出：-1（找不到返回-1）

# 指定开始位置查找
print(str.find("Hello", 5))     # 输出：13（从索引5开始查找）

# 指定开始和结束位置查找
print(str.find("Hello", 5, 15)) # 输出：13
print(str.find("Hello", 5, 10)) # 输出：-1（在指定范围内找不到）