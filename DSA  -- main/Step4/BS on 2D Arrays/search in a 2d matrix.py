matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

row=len(matrix)
col=len(matrix[0])

def BS(matrix,row,col):
    low=0
    high=col-1
    while low<=high:
        mid=(low+high)//2
        if matrix[row][mid]==target:
            return True
        elif matrix[row][mid]<target:
            low=mid+1
        else:
            high=mid-1
    return False

low=0
high=row-1

while low<=high:
    mid=(low+high)//2
    if target<matrix[mid][0]:
        high=mid-1
    elif target>matrix[mid][-1]:
        low=mid+1
    else:
        if BS(matrix,mid,col):
            print("Found at row:", mid)
        else:
            print("Not found")
        break


