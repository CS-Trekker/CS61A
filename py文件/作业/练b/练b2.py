N = float(input())
if 0 <= N < 5:
    N = 2.5-N
elif 5 <= N < 10:
    N = 2-1.5*(N-3)*(N-3)
elif 10 <= N < 20:
    N = N/2-1.5
print(f"{N:.3f}")