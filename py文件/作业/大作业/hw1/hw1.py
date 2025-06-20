#胡豪 大作业 12月3日

datas = open("students.txt","r",encoding = "utf-8")
lines = datas.readlines()
datas.close()
del lines[0]
# print(lines)

new_lines = [list(i.strip("\n").split(",")) for i in lines]
# print(new_lines)

for i in new_lines:
    xuehao = i[1]
    cards = open(xuehao+".txt","w",encoding = "utf-8")
    cards.write(f'''大学英语四级考试
CET4
准考证
准考证号：{i[1]}
考生姓名：{i[0]}
考场号：{i[2][1]}
座位号：{i[3]}
学校名称：{i[4]}
学院系别：{i[5]}
备注：考试须携带准考证、学生证、身份证参加考试
''')
    cards.close()
