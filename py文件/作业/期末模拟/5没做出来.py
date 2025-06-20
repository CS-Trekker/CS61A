n,m = map(int,input().split())
sx,sy = map(int,input().split())
matrix = []
for i in range(n):
    row = [x for x in input()]
    matrix.append(row)
# print(matrix)
# [['.', '.', '.', '.'], ['.', '.', '*', '.'], ['.', '.', '.', '!'], ['.', '*', '.', '*'], ['.', '.', '.', '*']]


block_flag = False
q = int(input())
count = 0
for i in range(q):
    xingdong = input()
    if xingdong == "rest":
        pass
    else:
        fang,bu = xingdong.split()
        bu = int(bu)

        if fang == "right":
            sy += bu
            for i in range(sy+1, sy + bu + 1):
                if 1<=i<=m:
                    if matrix[sx-1][i-1] == "!":
                        block_flag = True
                        break
                    if matrix[sx-1][i-1] == "*":
                        count += 1

        elif fang == "left":
            sy -= bu
            for i in range(sy+1, sy - bu + 1):
                if 1 <= i <= m:
                    if matrix[sx-1][i-1] == "!":
                        block_flag = True
                        break
                    if matrix[sx-1][i-1] == "*":
                        count += 1

        elif fang == "up":
            sx -= bu
            for i in range(sx+1, sx - bu + 1):
                if 1<=i<=n:
                    if matrix[i-1][sy-1] == "!":
                        block_flag = True
                        break
                    if matrix[i - 1][sy - 1] == "*":
                        count += 1

        elif fang == "down":
            sx += bu
            for i in range(sx+1, sx + bu + 1):
                if 1 <= i <= n:
                    if matrix[i][sy-1] == "!":
                        block_flag = True
                        break
                    if matrix[i][sy - 1] == "*":
                        count += 1
    # print(sx,sy)
# print(sx,sy)
# print(block_flag)
# print(sx,sy)
if block_flag or sx < 1 or sx > n or sy <1 or sy > m:
    print("invalid")
else:
    print("valid")
    print(count)