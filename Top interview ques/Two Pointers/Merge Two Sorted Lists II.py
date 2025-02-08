#Given two sorted integer arrays A and B, merge B into A as one sorted array.

def merge(A, B):
    n = len(A)
    m = len(B)
    
    A.extend([0] * m)  
    
    i = n - 1  
    j = m - 1  
    k = n + m - 1 
    
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1
    

