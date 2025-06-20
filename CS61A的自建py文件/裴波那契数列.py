def fib(n):
    k = 0
    pre = 1
    cur = 0
    while k < n:
        pre, cur = cur, cur + pre
        k += 1
    return cur

n = int(input())
print(fib(n))