n = int(input())
matrix = []
for i in range(n):
    li = list(input())
    matrix.append(li)
matrix.insert(0,["#"]*(n+2))
matrix.append(["#"]*(n+2))
for i in range(1,n+1):
    matrix[i].insert(0,"#")
    matrix[i].append("#")
# print(matrix)

def f(m,matrix):
    for i in range(m-1):
        new = []
        for k in range(n+2):
            for j in range(n+2):
                if matrix[k][j] == "." and ( matrix[k][j-1] == "@" or  matrix[k][j+1] == "@" or matrix[k-1][j] == "@" or  matrix[k+1][j] =="@"):
                    new.append((k,j))
        for (k,j) in new:
            matrix[k][j] = "@"
        # for g in matrix:
        #     print(g)

    count = 0
    for k in range(1,n+1):
        for j in range(1,n+1):
            if matrix[k][j] == "@":
                count += 1
    return count

m= int(input())
print(f(m,matrix))