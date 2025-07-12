q = float(input("请输入一个小数："))  # 输入一个小数
n = int(input("请输入一个非负整数："))  # 输入一个非负整数

result = round(q, n)  # 四舍五入并保留n位小数

print(result)  # 打印结果