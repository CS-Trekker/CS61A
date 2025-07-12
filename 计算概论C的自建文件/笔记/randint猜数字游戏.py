import random

num = random.randint(1, 100)
guess = 0
tries = 0

print("欢迎来到猜数字小游戏!")
print("在1-100内猜一个数，猜对了有奖励哦^_^")

c = int(input("你想在几次内猜出来："))

while guess != num and tries <= c:
    guess = int(input("请输入你猜的数字："))
    tries += 1
    if guess < num:
        print("猜小了")
    elif guess > num:
        print("猜大了")
    else:
        print("猜中了！恭喜你！")
        break

if tries > c:
    print("你没有机会了，你输了")
print("这个数字是：", num)
