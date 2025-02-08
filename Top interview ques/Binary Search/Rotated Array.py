#Suppose a sorted array A is rotated at some pivot unknown to you befo  rehand. Find the minimum element.

def findMin(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2
        if A[mid] > A[high]:
            low = mid + 1
        else:
            high = mid
    return A[low]