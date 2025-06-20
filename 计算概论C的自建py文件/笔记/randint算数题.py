import random

print("欢迎来到加法练习！")
correct = 0

while True:
    print("请计算下面算式的结果，输入“退出”结束练习")
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("%d + %d = " % (a, b), end="")
    n = input()
    if n == "退出":
        print("你一共做对了%d道题。" % correct)
        break
    if int(n) == a + b:
        print("恭喜你答对了！")
        correct += 1
    else:
        print("不好意思你答错了！")
