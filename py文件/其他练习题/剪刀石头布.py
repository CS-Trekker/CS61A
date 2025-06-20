N,NA,NB = map(int,input().split())

A_lst = []
B_lst = []

A_cyc = list(map(int,input().split()))
B_cyc = list(map(int,input().split()))

while len(A_lst) < N:
    A_lst.extend(A_cyc)
if len(A_lst) > N:
    A_lst = A_lst[:N]

# print(A_lst)

while len(B_lst) < N:
    B_lst.extend(B_cyc)
if len(B_lst) > N:
    B_lst = B_lst[:N]

# print(B_lst)

A_mark = 0
B_mark = 0

for i in range(N):
    if A_lst[i] == 0 and B_lst[i] == 2 or A_lst[i] == 2 and B_lst[i] == 5 or A_lst[i] == 5 and B_lst[i] == 0:
        A_mark += 1
    elif B_lst[i] == 0 and A_lst[i] == 2 or B_lst[i] == 2 and A_lst[i] == 5 or B_lst[i] == 5 and A_lst[i] == 0:
        B_mark += 1
    else:
        continue

if A_mark>B_mark:
    print("A")
elif B_mark>A_mark:
    print("B")
else:
    print("draw")
