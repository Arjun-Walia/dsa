matrix = [[0, 0, 1], [0, 0, 0],[1, 1, 0]]
row=len(matrix)
col=len(matrix[0])

def countOne(row):
    low = 0
    high = len(row) - 1
    while low <= high:
        mid = (low + high) // 2
        if row[mid] == 1:
            low = mid + 1
        else:
            high = mid - 1
    return low
cnt=0
for i in range(row):
    val=countOne(matrix[i])
    if val>cnt:
        cnt=val

print(cnt)
