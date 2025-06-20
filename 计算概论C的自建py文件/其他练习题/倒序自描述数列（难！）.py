# def f(n):
#     if n == 1:
#         return "1"
#     else:
#         # 获取前一项并倒序
#         reversed_i = f(n - 1)[::-1]
#
#         # 初始化结果列表
#         sequence = []
#         i = 0#i是指针
#
#         # 遍历倒序后的字符串
#         while i < len(reversed_i):
#             count = 1# 统计连续相同字符的数量
#             while i + 1 < len(reversed_i) and reversed_i[i] == reversed_i[i + 1]:
#                 count += 1
#                 i += 1
#             # 拼接 "次数+数字"
#             sequence.append(str(count) + reversed_i[i])
#             i += 1
#
#         # 返回新项
#         return "".join(sequence)
#
#
# # 输入与输出
# n = int(input())
# print(f(n))



def f(n):
    if n == 1:
        return "1"
    else:
        reversed_i = f(n-1)[::-1]
        # print(reversed_i)
        i = 0
        sequence = []
        while i < len(reversed_i):
            count = 1
            while i + 1 < len(reversed_i) and reversed_i[i] == reversed_i[i+1]:
                count += 1
                i += 1
            sequence.append(str(count))
            sequence.append(reversed_i[i])
            i += 1
        return "".join(sequence)

n = int(input())
print(f(n))

