M,N= map(int,input().split())
matrix = []
for i in range(M):
    li = list(input())
    matrix.append(li)
matrix.insert(0,["2"]*(N+2))
matrix.append(["2"]*(N+2))
for i in range(1,M+1):
    matrix[i].insert(0,"2")
    matrix[i].append("2")
# print(matrix)

def f(m,matrix):
    for i in range(m):
        new = []
        for k in range(M+2):
            for j in range(N+2):
                if matrix[k][j] == "0" and ( matrix[k][j-1] == "1" or  matrix[k][j+1] == "1" or matrix[k-1][j] == "1" or  matrix[k+1][j] =="1"):
                    new.append((k,j))
        for (k,j) in new:
            matrix[k][j] = "1"
        # for g in matrix:
        #     print(g)

    count = 0
    for k in range(1,M+1):
        for j in range(1,N+1):
            if matrix[k][j] == "1":
                count += 1
    return count

t = int(input())
print(f(t,matrix))