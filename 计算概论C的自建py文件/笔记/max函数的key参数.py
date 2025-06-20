dic = {"a" : 898,"b" : 978,"c" : 272}
max_letter = max(dic,key = dic.get)
print(max_letter)

#key是函数，表示把dic这个可迭代对象中的每个元素
# 进行函数处理，然后按照处理后的结果返回最大值