matrix = [[1,2,3],[4,5,6],[7,8,9]]

#brute force code

n=len(matrix)
ans=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        ans[j][n-1-i]=matrix[i][j]

print(ans)

#optimal code

n=len(matrix)

for i in range(n):
    for j in range(i):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()
print(matrix)
