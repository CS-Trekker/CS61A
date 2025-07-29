import re

# 示例 1：贪婪匹配（尽可能多地匹配）
s1 = "aabababababaeba什么东西nb"
result_greedy = re.findall("a.*b", s1)
print("贪婪匹配：", result_greedy)  # 输出：['aababababab']

# 示例 2：非贪婪（最小）匹配（尽可能少地匹配）
result_non_greedy = re.findall("a.*?b", s1)
print("非贪婪匹配：", result_non_greedy)  # 输出：['aab', 'ab', 'ab', 'ab']

# 示例 3：使用捕获组，提取两个字符之间的内容
result_capture_group = re.findall("a(.*?)b", s1)
print("捕获组匹配：", result_capture_group)  
# 输出：['a', '', '', 'a', '', '', 'a', '', '', 'a', '', '', 'e']

# 示例 4：re.match 和 re.search 的区别演示
print("re.match 示例：")
print(re.match("py.", "python"))      # 匹配成功，返回 Match 对象
print(re.match("py.$", "python"))     # 匹配失败，返回 None（末尾不是单个字符）

print("re.search 示例：")
print(re.search("a", "jianndsi"))     # 匹配成功，返回 Match 对象
print(re.search("^a", "jianndsi"))    # 匹配失败，开头不是 a，返回 None
print(re.search("^a", "ji anndsi"))   # 同上，仍返回 None

# 示例 5：re.search 返回的 Match 对象演示
text = "jianndsi"
m = re.search("a.*d", text)

if m:
    print("匹配到的字符串：", m.group())  # 获取匹配到的字符串
    print("起始位置：", m.start())         # 匹配字符串起始索引
    print("结束位置：", m.end())           # 匹配字符串结束索引（不含）
    print("匹配范围：", m.span())          # 返回匹配起止索引的元组
else:
    print("没匹配到")

# 示例 6：从文本中提取位于尖括号内、无前导0且不超过3位的整数（或单独的0）
s2 = "abc<123>cd<0456>,78,123<3554>1a<38>ab<08>,1<0>111cd<3>"
pattern = r"<(0|[1-9]\d{0,2})>"
matches = re.findall(pattern, s2)

print("提取的符合条件的数字：", matches)
# 输出：['123', '38', '0', '3']
