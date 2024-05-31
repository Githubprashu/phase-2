#ADJACENCY MATRIX

n,m = map(int,input().split())
matrix=[]
for i in range(n):
    row = [0]*n
    matrix.append(row)

print(matrix)
for i in range(m):
    u,v = map(int,input().split())
    matrix[u][v]=1
    matrix[v][u]=1

print(matrix)