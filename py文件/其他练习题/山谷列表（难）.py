N = int(input())  # 输入需要判断的列表个数

# 遍历每个列表
for _ in range(N):
    arr = list(map(int, input().split()))  # 输入列表

    # 长度小于3，不可能是山谷
    if len(arr) < 3:
        print("NO")
        continue

    # 寻找递减部分的结束位置
    i = 1
    while i < len(arr) and arr[i] < arr[i - 1]:
        i += 1

    # 如果递减部分的结束位置是列表的第一个或最后一个位置，直接NO
    if i == 1 or i == len(arr):
        print("NO")
        continue

    # 寻找递增部分
    while i < len(arr) and arr[i] > arr[i - 1]:
        i += 1

    # 如果循环结束时i正好遍历到列表末尾，说明是山谷
    if i == len(arr):
        print("YES")
    else:
        print("NO")