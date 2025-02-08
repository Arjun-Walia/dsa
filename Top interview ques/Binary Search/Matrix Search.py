#Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A. 

def searchMatrix(A, B):
    if not A or not A[0]:
        return 0
    
    rows = len(A)
    cols = len(A[0])
    
    low = 0
    high = rows * cols - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = A[mid // cols][mid % cols]
        
        if mid_value == B:
            return 1
        elif mid_value < B:
            low = mid + 1
        else:
            high = mid - 1
    
    return 0

