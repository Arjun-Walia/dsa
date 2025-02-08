#Given a large number represent in the form of an integer array A, where each element is a digit. 
#You have to find whether there exists any permutation of the array A such that the number becomes divisible by 60.

def divisibleBy60(A):
    if len(A)==1 and A[0]==0:
        return 1
    if 0 not in A:
        return 0
    
    if sum(A) % 3 != 0:
        return 0
    
    even_digits = [digit for digit in A if digit % 2 == 0 and digit != 0]
    if not even_digits:
        return 0
    
    return 1
