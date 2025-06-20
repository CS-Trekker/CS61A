def w(n, m):
    lst = list(range(1, n + 1))
    start = 0  # 从第一个猴子开始
    while len(lst) > 1:
        dead = (start + m - 1) % len(lst)  # 计算要淘汰的猴子
        lst.pop(dead)  # 淘汰猴子
        start = dead  # 更新起始位置
    return lst[0]  # 返回最后剩下的猴王

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print(w(n, m))

def w(n, m):
    # 如果只剩一个猴子，它就是猴王
    if n == 1:
        return 1
    # 递推公式：f(n,m) = (f(n-1,m) + m - 1) % n + 1
    return (w(n - 1, m) + m - 1) % n + 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print(w(n, m))