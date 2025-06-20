#横行是row,竖列是column
#matrix里有几个列表元素，就有多少row
#每个列表里又有多少元素
m,n = map(int,input().split())
matrix = []
for i in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
# print(matrix)

for i in matrix:
    i.append(0)
    i.insert(0,0)
matrix.append([0]*(n+2))
matrix.insert(0,[0]*(n+2))
# print(matrix)

peak = []
for i in range(1,m+1):
    for j in range(1,n+1):
        if matrix[i][j] >= matrix[i][j-1] and matrix[i][j] >= matrix[i][j+1] and matrix[i][j] >= matrix[i-1][j] and matrix[i][j] >= matrix[i+1][j]:
            peak.append([i-1,j-1])
peak.sort(key=lambda x:(x[0],x[1]))
# print(peak)
for i in peak:
    print(*i)