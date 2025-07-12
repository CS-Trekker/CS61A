# 判断字符串是否只包含字母和/或数字
print("Hello123".isalnum())   # 输出：True
print("abc".isalnum())        # 输出：True
print("123".isalnum())        # 输出：True
print("你好123".isalnum())    # 输出：True

# 包含其他字符返回False
print("Hello 123".isalnum())  # 输出：False（因为有空格）
print("Hello!123".isalnum()) # 输出：False（因为有感叹号）


# 字符串是否只包含数字
print('123'.isdigit())  # 输出：True
print('123abc'.isdigit())  # 输出：False
print('abc123'.isdigit())  # 输出：False
print('123.45'.isdigit())  # 输出：False（小数点不是数字）
print(''.isdigit())  # 输出：False


# 判断字符串是否只包含字母
print("Hello".isalpha())      # 输出：True
print("你好".isalpha())       # 输出：True（中文字符也算字母）

# 包含空格、数字或标点符号返回False
print("Hello World".isalpha())  # 输出：False（因为有空格）
print("Hello123".isalpha())     # 输出：False（因为有数字）
print("Hello!".isalpha())       # 输出：False（因为有感叹号）



# 判断字符串里的字母是否都是小写
print("hello".islower())          # 输出：True
print("hello123".islower())       # 输出：True（数字不影响判断）
print("hello!".islower())         # 输出：True（标点符号不影响判断）

# 包含大写字母返回False
print("Hello".islower())          # 输出：False
print("HELLO".islower())          # 输出：False