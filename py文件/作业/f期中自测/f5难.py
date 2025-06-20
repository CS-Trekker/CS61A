N = int(input())
matrix = []
for i in range(N):
    lst = list(map(int,input().split()))
    matrix.append(lst)

num = 0
for i in range(1,N-1):
    for k in range(1,N-1):
        if matrix[i][k]+50 <= matrix[i][k-1] and matrix[i][k]+50 <= matrix[i][k+1] and matrix[i][k]+50 <= matrix[i-1][k] and matrix[i][k]+50 <= matrix[i+1][k]:
            num += 1
print(num)